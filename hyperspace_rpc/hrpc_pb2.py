# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hrpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import (
    descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="hrpc.proto",
    package="hrpc",
    syntax="proto2",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\nhrpc.proto\x12\x04hrpc\x1a google/protobuf/descriptor.proto"\x06\n\x04Void:2\n\x07service\x12\x1f.google.protobuf.ServiceOptions\x18\xd0\x86\x03 \x01(\r:0\n\x06method\x12\x1e.google.protobuf.MethodOptions\x18\xd1\x86\x03 \x01(\r',
    dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,],
)


SERVICE_FIELD_NUMBER = 50000
service = _descriptor.FieldDescriptor(
    name="service",
    full_name="hrpc.service",
    index=0,
    number=50000,
    type=13,
    cpp_type=3,
    label=1,
    has_default_value=False,
    default_value=0,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)
METHOD_FIELD_NUMBER = 50001
method = _descriptor.FieldDescriptor(
    name="method",
    full_name="hrpc.method",
    index=1,
    number=50001,
    type=13,
    cpp_type=3,
    label=1,
    has_default_value=False,
    default_value=0,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
)


_VOID = _descriptor.Descriptor(
    name="Void",
    full_name="hrpc.Void",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=54,
    serialized_end=60,
)

DESCRIPTOR.message_types_by_name["Void"] = _VOID
DESCRIPTOR.extensions_by_name["service"] = service
DESCRIPTOR.extensions_by_name["method"] = method
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Void = _reflection.GeneratedProtocolMessageType(
    "Void",
    (_message.Message,),
    {
        "DESCRIPTOR": _VOID,
        "__module__": "hrpc_pb2"
        # @@protoc_insertion_point(class_scope:hrpc.Void)
    },
)
_sym_db.RegisterMessage(Void)

google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
    service
)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(method)

# @@protoc_insertion_point(module_scope)