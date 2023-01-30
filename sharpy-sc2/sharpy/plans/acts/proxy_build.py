from typing import Optional

from sharpy.plans.acts import ActBase
from sharpy.managers.core.roles import UnitTask
from sc2.ids.unit_typeid import UnitTypeId
from sc2.position import Point2
from sc2.unit import Unit
from sharpy.interfaces import IZoneManager
from sc2.ids.unit_typeid import UnitTypeId


class ProxyBuild(ActBase):
    def __init__(self, unit_type: UnitTypeId, only_once: bool = True):
        super().__init__()
        self.position = None
        self.unit_type = unit_type
        self.only_once = only_once
        self.builder_tag: Optional[int] = None
        self.finished = False

    async def start(self, knowledge: "Knowledge"):
        await super().start(knowledge)

    async def execute(self) -> bool:

        if self.finished:
            return True

        if self.position is None:
            self.position = self.knowledge.get_required_manager(IZoneManager). \
                    enemy_expansion_zones[2].center_location

        for building in self.cache.own(self.unit_type):  # type: Unit
            if building.distance_to(self.position) < 20:
                if self.only_once:
                    self.position = None
                    self.finished = True
                return True

        position = self.position

        worker = self.get_worker_builder(position, self.builder_tag)
        if worker is None:
            return True  # No worker to build with.

        if self.knowledge.can_afford(self.unit_type) and worker.distance_to(position) < 5:
            self.position = await self.ai.find_placement(self.unit_type, self.position, 20)
            position = self.position

            if position is not None:
                self.print(f"Building {self.unit_type.name} to {position}")
                worker.build(self.unit_type, position)
                self.set_worker(worker)
            else:
                self.print(f"Could not build {self.unit_type.name} to {position}")
        else:
            unit = self.ai._game_data.units[self.unit_type.value]
            cost = self.ai._game_data.calculate_ability_cost(unit.creation_ability)

            d = worker.distance_to(position)
            time = d / worker.movement_speed
            if self.ai.minerals - self.knowledge.reserved_minerals > (
                    cost.minerals - 10 * time
            ) and self.ai.vespene - self.knowledge.reserved_gas > (cost.vespene - time):

                if worker is not None:
                    self.set_worker(worker)
                    worker.move(position)

            self.knowledge.reserve(cost.minerals, cost.vespene)

        return False

    def set_worker(self, worker: Unit):
        self.roles.set_task(UnitTask.Building, worker)
        self.builder_tag = worker.tag
