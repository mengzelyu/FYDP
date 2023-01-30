# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: s2clientprotocol/score.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cs2clientprotocol/score.proto\x12\x0eSC2APIProtocol\"\xa8\x01\n\x05Score\x12\x33\n\nscore_type\x18\x06 \x01(\x0e\x32\x1f.SC2APIProtocol.Score.ScoreType\x12\r\n\x05score\x18\x07 \x01(\x05\x12\x33\n\rscore_details\x18\x08 \x01(\x0b\x32\x1c.SC2APIProtocol.ScoreDetails\"&\n\tScoreType\x12\x0e\n\nCurriculum\x10\x01\x12\t\n\x05Melee\x10\x02\"h\n\x14\x43\x61tegoryScoreDetails\x12\x0c\n\x04none\x18\x01 \x01(\x02\x12\x0c\n\x04\x61rmy\x18\x02 \x01(\x02\x12\x0f\n\x07\x65\x63onomy\x18\x03 \x01(\x02\x12\x12\n\ntechnology\x18\x04 \x01(\x02\x12\x0f\n\x07upgrade\x18\x05 \x01(\x02\"B\n\x11VitalScoreDetails\x12\x0c\n\x04life\x18\x01 \x01(\x02\x12\x0f\n\x07shields\x18\x02 \x01(\x02\x12\x0e\n\x06\x65nergy\x18\x03 \x01(\x02\"\x8a\n\n\x0cScoreDetails\x12\x1c\n\x14idle_production_time\x18\x01 \x01(\x02\x12\x18\n\x10idle_worker_time\x18\x02 \x01(\x02\x12\x19\n\x11total_value_units\x18\x03 \x01(\x02\x12\x1e\n\x16total_value_structures\x18\x04 \x01(\x02\x12\x1a\n\x12killed_value_units\x18\x05 \x01(\x02\x12\x1f\n\x17killed_value_structures\x18\x06 \x01(\x02\x12\x1a\n\x12\x63ollected_minerals\x18\x07 \x01(\x02\x12\x19\n\x11\x63ollected_vespene\x18\x08 \x01(\x02\x12 \n\x18\x63ollection_rate_minerals\x18\t \x01(\x02\x12\x1f\n\x17\x63ollection_rate_vespene\x18\n \x01(\x02\x12\x16\n\x0espent_minerals\x18\x0b \x01(\x02\x12\x15\n\rspent_vespene\x18\x0c \x01(\x02\x12\x37\n\tfood_used\x18\r \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12=\n\x0fkilled_minerals\x18\x0e \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12<\n\x0ekilled_vespene\x18\x0f \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12;\n\rlost_minerals\x18\x10 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12:\n\x0clost_vespene\x18\x11 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12\x44\n\x16\x66riendly_fire_minerals\x18\x12 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12\x43\n\x15\x66riendly_fire_vespene\x18\x13 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12;\n\rused_minerals\x18\x14 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12:\n\x0cused_vespene\x18\x15 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12\x41\n\x13total_used_minerals\x18\x16 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12@\n\x12total_used_vespene\x18\x17 \x01(\x0b\x32$.SC2APIProtocol.CategoryScoreDetails\x12=\n\x12total_damage_dealt\x18\x18 \x01(\x0b\x32!.SC2APIProtocol.VitalScoreDetails\x12=\n\x12total_damage_taken\x18\x19 \x01(\x0b\x32!.SC2APIProtocol.VitalScoreDetails\x12\x37\n\x0ctotal_healed\x18\x1a \x01(\x0b\x32!.SC2APIProtocol.VitalScoreDetails\x12\x13\n\x0b\x63urrent_apm\x18\x1b \x01(\x02\x12\x1d\n\x15\x63urrent_effective_apm\x18\x1c \x01(\x02')



_SCORE = DESCRIPTOR.message_types_by_name['Score']
_CATEGORYSCOREDETAILS = DESCRIPTOR.message_types_by_name['CategoryScoreDetails']
_VITALSCOREDETAILS = DESCRIPTOR.message_types_by_name['VitalScoreDetails']
_SCOREDETAILS = DESCRIPTOR.message_types_by_name['ScoreDetails']
_SCORE_SCORETYPE = _SCORE.enum_types_by_name['ScoreType']
Score = _reflection.GeneratedProtocolMessageType('Score', (_message.Message,), {
  'DESCRIPTOR' : _SCORE,
  '__module__' : 's2clientprotocol.score_pb2'
  # @@protoc_insertion_point(class_scope:SC2APIProtocol.Score)
  })
_sym_db.RegisterMessage(Score)

CategoryScoreDetails = _reflection.GeneratedProtocolMessageType('CategoryScoreDetails', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORYSCOREDETAILS,
  '__module__' : 's2clientprotocol.score_pb2'
  # @@protoc_insertion_point(class_scope:SC2APIProtocol.CategoryScoreDetails)
  })
_sym_db.RegisterMessage(CategoryScoreDetails)

VitalScoreDetails = _reflection.GeneratedProtocolMessageType('VitalScoreDetails', (_message.Message,), {
  'DESCRIPTOR' : _VITALSCOREDETAILS,
  '__module__' : 's2clientprotocol.score_pb2'
  # @@protoc_insertion_point(class_scope:SC2APIProtocol.VitalScoreDetails)
  })
_sym_db.RegisterMessage(VitalScoreDetails)

ScoreDetails = _reflection.GeneratedProtocolMessageType('ScoreDetails', (_message.Message,), {
  'DESCRIPTOR' : _SCOREDETAILS,
  '__module__' : 's2clientprotocol.score_pb2'
  # @@protoc_insertion_point(class_scope:SC2APIProtocol.ScoreDetails)
  })
_sym_db.RegisterMessage(ScoreDetails)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCORE._serialized_start=49
  _SCORE._serialized_end=217
  _SCORE_SCORETYPE._serialized_start=179
  _SCORE_SCORETYPE._serialized_end=217
  _CATEGORYSCOREDETAILS._serialized_start=219
  _CATEGORYSCOREDETAILS._serialized_end=323
  _VITALSCOREDETAILS._serialized_start=325
  _VITALSCOREDETAILS._serialized_end=391
  _SCOREDETAILS._serialized_start=394
  _SCOREDETAILS._serialized_end=1684
# @@protoc_insertion_point(module_scope)
