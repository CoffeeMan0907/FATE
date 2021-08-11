# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-imputation-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feature-imputation-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\033FeatureImputationParamProto'),
  serialized_pb=_b('\n\x1e\x66\x65\x61ture-imputation-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xc2\x04\n\x13\x46\x65\x61tureImputerParam\x12s\n\x15missing_replace_value\x18\x01 \x03(\x0b\x32T.com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueEntry\x12o\n\x13missing_value_ratio\x18\x02 \x03(\x0b\x32R.com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingValueRatioEntry\x12|\n\x1amissing_replace_value_type\x18\x03 \x03(\x0b\x32X.com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueTypeEntry\x12\x11\n\tskip_cols\x18\x04 \x03(\t\x1a:\n\x18MissingReplaceValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16MissingValueRatioEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a>\n\x1cMissingReplaceValueTypeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"|\n\x16\x46\x65\x61tureImputationParam\x12\x0e\n\x06header\x18\x01 \x03(\t\x12R\n\rimputer_param\x18\x02 \x01(\x0b\x32;.com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParamB\x1d\x42\x1b\x46\x65\x61tureImputationParamProtob\x06proto3')
)




_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY = _descriptor.Descriptor(
  name='MissingReplaceValueEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=531,
)

_FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY = _descriptor.Descriptor(
  name='MissingValueRatioEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingValueRatioEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingValueRatioEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingValueRatioEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=589,
)

_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY = _descriptor.Descriptor(
  name='MissingReplaceValueTypeEntry',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueTypeEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueTypeEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueTypeEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=591,
  serialized_end=653,
)

_FEATUREIMPUTERPARAM = _descriptor.Descriptor(
  name='FeatureImputerParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missing_replace_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.missing_replace_value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_value_ratio', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.missing_value_ratio', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missing_replace_value_type', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.missing_replace_value_type', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_cols', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.skip_cols', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY, _FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY, _FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=653,
)


_FEATUREIMPUTATIONPARAM = _descriptor.Descriptor(
  name='FeatureImputationParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputationParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputationParam.header', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imputer_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.FeatureImputationParam.imputer_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=779,
)

_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY.containing_type = _FEATUREIMPUTERPARAM
_FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY.containing_type = _FEATUREIMPUTERPARAM
_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY.containing_type = _FEATUREIMPUTERPARAM
_FEATUREIMPUTERPARAM.fields_by_name['missing_replace_value'].message_type = _FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY
_FEATUREIMPUTERPARAM.fields_by_name['missing_value_ratio'].message_type = _FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY
_FEATUREIMPUTERPARAM.fields_by_name['missing_replace_value_type'].message_type = _FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY
_FEATUREIMPUTATIONPARAM.fields_by_name['imputer_param'].message_type = _FEATUREIMPUTERPARAM
DESCRIPTOR.message_types_by_name['FeatureImputerParam'] = _FEATUREIMPUTERPARAM
DESCRIPTOR.message_types_by_name['FeatureImputationParam'] = _FEATUREIMPUTATIONPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeatureImputerParam = _reflection.GeneratedProtocolMessageType('FeatureImputerParam', (_message.Message,), {

  'MissingReplaceValueEntry' : _reflection.GeneratedProtocolMessageType('MissingReplaceValueEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY,
    '__module__' : 'feature_imputation_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueEntry)
    })
  ,

  'MissingValueRatioEntry' : _reflection.GeneratedProtocolMessageType('MissingValueRatioEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY,
    '__module__' : 'feature_imputation_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingValueRatioEntry)
    })
  ,

  'MissingReplaceValueTypeEntry' : _reflection.GeneratedProtocolMessageType('MissingReplaceValueTypeEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY,
    '__module__' : 'feature_imputation_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam.MissingReplaceValueTypeEntry)
    })
  ,
  'DESCRIPTOR' : _FEATUREIMPUTERPARAM,
  '__module__' : 'feature_imputation_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureImputerParam)
  })
_sym_db.RegisterMessage(FeatureImputerParam)
_sym_db.RegisterMessage(FeatureImputerParam.MissingReplaceValueEntry)
_sym_db.RegisterMessage(FeatureImputerParam.MissingValueRatioEntry)
_sym_db.RegisterMessage(FeatureImputerParam.MissingReplaceValueTypeEntry)

FeatureImputationParam = _reflection.GeneratedProtocolMessageType('FeatureImputationParam', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREIMPUTATIONPARAM,
  '__module__' : 'feature_imputation_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureImputationParam)
  })
_sym_db.RegisterMessage(FeatureImputationParam)


DESCRIPTOR._options = None
_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUEENTRY._options = None
_FEATUREIMPUTERPARAM_MISSINGVALUERATIOENTRY._options = None
_FEATUREIMPUTERPARAM_MISSINGREPLACEVALUETYPEENTRY._options = None
# @@protoc_insertion_point(module_scope)
