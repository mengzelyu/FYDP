from random import choice
from typing import Callable, Tuple, List, Dict, Optional

from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.data import Race
from sharpy.knowledges import KnowledgeBot
from sharpy.managers import ManagerBase

from sharpy.managers.extensions import DataManager, BuildDetector
from sharpy.managers.extensions.build_detector import EnemyRushBuild
from sharpy.plans.protoss import *

from .build_orders.pvp.start_up import pvp_start_up
from .build_orders.pvp.counterCannonRush import counterCannonRush
from .build_orders.pvp.counterNexusFirst import counterNexusFirst


class ProtossBot(KnowledgeBot):
    data_manager: DataManager

    def __init__(self, build_name: str = "default"):
        super().__init__("FYDP")
        self.conceded = False
        self.builds: Dict[str, Callable[[], BuildOrder]] = {
            "pvp": lambda: self.pvp_build(),
            "pvz": lambda: self.pvz_build(),
            "pvt": lambda: self.pvt_build(),
            "pvr": lambda: self.pvr_build()
        }
        self.build_name = build_name

    def configure_managers(self) -> Optional[List[ManagerBase]]:
        return [BuildDetector()]

    async def create_plan(self) -> BuildOrder:
        if self.build_name == "default":
            if self.knowledge.enemy_race == Race.Protoss:
                self.build_name = "pvp"
            elif self.knowledge.enemy_race == Race.Zerg:
                self.build_name = "pvz"
            elif self.knowledge.enemy_race == Race.Terran:
                self.build_name = "pvt"
            else:
                self.build_name = self.build_name = "pvr"

        self.data_manager.set_build(self.build_name)
        return self.builds[self.build_name]()

    async def on_step(self, iteration):
        return await super().on_step(iteration)

    def pvp_build(self) -> BuildOrder:
        return BuildOrder(
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.Start, pvp_start_up()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.WorkerRush, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.CannonRush, counterCannonRush()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.NexusFirst, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.SingleGate, counterNexusFirst()),

            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.ProxyZealots, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.ProxyRobo, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.ProxyVoid, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.ProxyFourGate, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.PotentialProxy, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.RoboExpand, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.StargateExpand, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.TwilightExpand, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.PVPMidGameMacro, counterNexusFirst()),
            Step(lambda k: k.build_detector.rush_build == EnemyRushBuild.PVPLateGameMacro, counterNexusFirst()),



        )

    def pvt_build(self) -> BuildOrder:
        return self.pvp_build()

    def pvz_build(self) -> BuildOrder:
        return self.pvp_build()

    def pvr_build(self) -> BuildOrder:
        return self.pvp_build()
