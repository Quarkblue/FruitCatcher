# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/landmarks_refinement_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/landmarks_refinement_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@mediapipe/calculators/util/landmarks_refinement_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xdd\x05\n$LandmarksRefinementCalculatorOptions\x12N\n\nrefinement\x18\x01 \x03(\x0b\x32:.mediapipe.LandmarksRefinementCalculatorOptions.Refinement\x1a\x11\n\x0fZRefinementNone\x1a\x11\n\x0fZRefinementCopy\x1a\x37\n\x18ZRefinementAssignAverage\x12\x1b\n\x13indexes_for_average\x18\x01 \x03(\x05\x1a\xab\x02\n\x0bZRefinement\x12O\n\x04none\x18\x01 \x01(\x0b\x32?.mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementNoneH\x00\x12O\n\x04\x63opy\x18\x02 \x01(\x0b\x32?.mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementCopyH\x00\x12\x62\n\x0e\x61ssign_average\x18\x03 \x01(\x0b\x32H.mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementAssignAverageH\x00\x42\x16\n\x14z_refinement_options\x1ax\n\nRefinement\x12\x17\n\x0findexes_mapping\x18\x01 \x03(\x05\x12Q\n\x0cz_refinement\x18\x02 \x01(\x0b\x32;.mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement2^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xa2\x9c\x8e\xb6\x01 \x01(\x0b\x32/.mediapipe.LandmarksRefinementCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTNONE = _descriptor.Descriptor(
  name='ZRefinementNone',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementNone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=255,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTCOPY = _descriptor.Descriptor(
  name='ZRefinementCopy',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementCopy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=274,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTASSIGNAVERAGE = _descriptor.Descriptor(
  name='ZRefinementAssignAverage',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementAssignAverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indexes_for_average', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementAssignAverage.indexes_for_average', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=331,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT = _descriptor.Descriptor(
  name='ZRefinement',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='none', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement.none', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='copy', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement.copy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assign_average', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement.assign_average', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='z_refinement_options', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement.z_refinement_options',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=334,
  serialized_end=633,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT = _descriptor.Descriptor(
  name='Refinement',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions.Refinement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indexes_mapping', full_name='mediapipe.LandmarksRefinementCalculatorOptions.Refinement.indexes_mapping', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z_refinement', full_name='mediapipe.LandmarksRefinementCalculatorOptions.Refinement.z_refinement', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=755,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS = _descriptor.Descriptor(
  name='LandmarksRefinementCalculatorOptions',
  full_name='mediapipe.LandmarksRefinementCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='refinement', full_name='mediapipe.LandmarksRefinementCalculatorOptions.refinement', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LandmarksRefinementCalculatorOptions.ext', index=0,
      number=381914658, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTNONE, _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTCOPY, _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTASSIGNAVERAGE, _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT, _LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=851,
)

_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTNONE.containing_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTCOPY.containing_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTASSIGNAVERAGE.containing_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['none'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTNONE
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['copy'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTCOPY
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['assign_average'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTASSIGNAVERAGE
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.containing_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options'].fields.append(
  _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['none'])
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['none'].containing_oneof = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options']
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options'].fields.append(
  _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['copy'])
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['copy'].containing_oneof = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options']
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options'].fields.append(
  _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['assign_average'])
_LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.fields_by_name['assign_average'].containing_oneof = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT.oneofs_by_name['z_refinement_options']
_LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT.fields_by_name['z_refinement'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT
_LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT.containing_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_LANDMARKSREFINEMENTCALCULATOROPTIONS.fields_by_name['refinement'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT
DESCRIPTOR.message_types_by_name['LandmarksRefinementCalculatorOptions'] = _LANDMARKSREFINEMENTCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LandmarksRefinementCalculatorOptions = _reflection.GeneratedProtocolMessageType('LandmarksRefinementCalculatorOptions', (_message.Message,), {

  'ZRefinementNone' : _reflection.GeneratedProtocolMessageType('ZRefinementNone', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTNONE,
    '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementNone)
    })
  ,

  'ZRefinementCopy' : _reflection.GeneratedProtocolMessageType('ZRefinementCopy', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTCOPY,
    '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementCopy)
    })
  ,

  'ZRefinementAssignAverage' : _reflection.GeneratedProtocolMessageType('ZRefinementAssignAverage', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENTASSIGNAVERAGE,
    '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions.ZRefinementAssignAverage)
    })
  ,

  'ZRefinement' : _reflection.GeneratedProtocolMessageType('ZRefinement', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS_ZREFINEMENT,
    '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions.ZRefinement)
    })
  ,

  'Refinement' : _reflection.GeneratedProtocolMessageType('Refinement', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS_REFINEMENT,
    '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions.Refinement)
    })
  ,
  'DESCRIPTOR' : _LANDMARKSREFINEMENTCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.util.landmarks_refinement_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LandmarksRefinementCalculatorOptions)
  })
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions)
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions.ZRefinementNone)
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions.ZRefinementCopy)
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions.ZRefinementAssignAverage)
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions.ZRefinement)
_sym_db.RegisterMessage(LandmarksRefinementCalculatorOptions.Refinement)

_LANDMARKSREFINEMENTCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LANDMARKSREFINEMENTCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LANDMARKSREFINEMENTCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
