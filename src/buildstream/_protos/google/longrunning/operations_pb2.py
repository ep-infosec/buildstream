# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/longrunning/operations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buildstream._protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from buildstream._protos.google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/longrunning/operations.proto\x12\x12google.longrunning\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\"\xa8\x01\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12#\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06result\"#\n\x13GetOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\\\n\x15ListOperationsRequest\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"d\n\x16ListOperationsResponse\x12\x31\n\noperations\x18\x01 \x03(\x0b\x32\x1d.google.longrunning.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"&\n\x16\x43\x61ncelOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x16\x44\x65leteOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\x8c\x04\n\nOperations\x12\x86\x01\n\x0eListOperations\x12).google.longrunning.ListOperationsRequest\x1a*.google.longrunning.ListOperationsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=operations}\x12x\n\x0cGetOperation\x12\'.google.longrunning.GetOperationRequest\x1a\x1d.google.longrunning.Operation\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=operations/**}\x12w\n\x0f\x44\x65leteOperation\x12*.google.longrunning.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\" \x82\xd3\xe4\x93\x02\x1a*\x18/v1/{name=operations/**}\x12\x81\x01\n\x0f\x43\x61ncelOperation\x12*.google.longrunning.CancelOperationRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/{name=operations/**}:cancel:\x01*B\x94\x01\n\x16\x63om.google.longrunningB\x0fOperationsProtoP\x01Z=google.golang.org/genproto/googleapis/longrunning;longrunning\xaa\x02\x12Google.LongRunning\xca\x02\x12Google\\LongRunningb\x06proto3')



_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_GETOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['GetOperationRequest']
_LISTOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListOperationsRequest']
_LISTOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListOperationsResponse']
_CANCELOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['CancelOperationRequest']
_DELETEOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteOperationRequest']
Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.Operation)
  })
_sym_db.RegisterMessage(Operation)

GetOperationRequest = _reflection.GeneratedProtocolMessageType('GetOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONREQUEST,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.GetOperationRequest)
  })
_sym_db.RegisterMessage(GetOperationRequest)

ListOperationsRequest = _reflection.GeneratedProtocolMessageType('ListOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSREQUEST,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.ListOperationsRequest)
  })
_sym_db.RegisterMessage(ListOperationsRequest)

ListOperationsResponse = _reflection.GeneratedProtocolMessageType('ListOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSRESPONSE,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.ListOperationsResponse)
  })
_sym_db.RegisterMessage(ListOperationsResponse)

CancelOperationRequest = _reflection.GeneratedProtocolMessageType('CancelOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELOPERATIONREQUEST,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.CancelOperationRequest)
  })
_sym_db.RegisterMessage(CancelOperationRequest)

DeleteOperationRequest = _reflection.GeneratedProtocolMessageType('DeleteOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOPERATIONREQUEST,
  '__module__' : 'google.longrunning.operations_pb2'
  # @@protoc_insertion_point(class_scope:google.longrunning.DeleteOperationRequest)
  })
_sym_db.RegisterMessage(DeleteOperationRequest)

_OPERATIONS = DESCRIPTOR.services_by_name['Operations']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.google.longrunningB\017OperationsProtoP\001Z=google.golang.org/genproto/googleapis/longrunning;longrunning\252\002\022Google.LongRunning\312\002\022Google\\LongRunning'
  _OPERATIONS.methods_by_name['ListOperations']._options = None
  _OPERATIONS.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002\027\022\025/v1/{name=operations}'
  _OPERATIONS.methods_by_name['GetOperation']._options = None
  _OPERATIONS.methods_by_name['GetOperation']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/{name=operations/**}'
  _OPERATIONS.methods_by_name['DeleteOperation']._options = None
  _OPERATIONS.methods_by_name['DeleteOperation']._serialized_options = b'\202\323\344\223\002\032*\030/v1/{name=operations/**}'
  _OPERATIONS.methods_by_name['CancelOperation']._options = None
  _OPERATIONS.methods_by_name['CancelOperation']._serialized_options = b'\202\323\344\223\002$\"\037/v1/{name=operations/**}:cancel:\001*'
  _OPERATION._serialized_start=171
  _OPERATION._serialized_end=339
  _GETOPERATIONREQUEST._serialized_start=341
  _GETOPERATIONREQUEST._serialized_end=376
  _LISTOPERATIONSREQUEST._serialized_start=378
  _LISTOPERATIONSREQUEST._serialized_end=470
  _LISTOPERATIONSRESPONSE._serialized_start=472
  _LISTOPERATIONSRESPONSE._serialized_end=572
  _CANCELOPERATIONREQUEST._serialized_start=574
  _CANCELOPERATIONREQUEST._serialized_end=612
  _DELETEOPERATIONREQUEST._serialized_start=614
  _DELETEOPERATIONREQUEST._serialized_end=652
  _OPERATIONS._serialized_start=655
  _OPERATIONS._serialized_end=1179
# @@protoc_insertion_point(module_scope)
