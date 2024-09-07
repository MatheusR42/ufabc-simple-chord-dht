from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[QueueType]
    SIMPLE: _ClassVar[QueueType]
    MULTIPLE: _ClassVar[QueueType]
NONE: QueueType
SIMPLE: QueueType
MULTIPLE: QueueType

class Queue(_message.Message):
    __slots__ = ("name", "type", "pendingMessages")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PENDINGMESSAGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: QueueType
    pendingMessages: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[QueueType, str]] = ..., pendingMessages: _Optional[int] = ...) -> None: ...

class RemoveQueueRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ListQueueResponse(_message.Message):
    __slots__ = ("queues",)
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    queues: _containers.RepeatedCompositeFieldContainer[Queue]
    def __init__(self, queues: _Optional[_Iterable[_Union[Queue, _Mapping]]] = ...) -> None: ...

class MessageType(_message.Message):
    __slots__ = ("text_message", "bytes_message")
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BYTES_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    text_message: str
    bytes_message: bytes
    def __init__(self, text_message: _Optional[str] = ..., bytes_message: _Optional[bytes] = ...) -> None: ...

class PublishMessagesRequest(_message.Message):
    __slots__ = ("queueName", "messages")
    QUEUENAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    queueName: str
    messages: _containers.RepeatedCompositeFieldContainer[MessageType]
    def __init__(self, queueName: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[MessageType, _Mapping]]] = ...) -> None: ...

class SignToQueuesRequest(_message.Message):
    __slots__ = ("queuesNames",)
    QUEUESNAMES_FIELD_NUMBER: _ClassVar[int]
    queuesNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, queuesNames: _Optional[_Iterable[str]] = ...) -> None: ...

class SignToQueuesResponse(_message.Message):
    __slots__ = ("queueName", "message")
    QUEUENAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    queueName: str
    message: MessageType
    def __init__(self, queueName: _Optional[str] = ..., message: _Optional[_Union[MessageType, _Mapping]] = ...) -> None: ...

class ConsumeMessageRequest(_message.Message):
    __slots__ = ("queueName",)
    QUEUENAME_FIELD_NUMBER: _ClassVar[int]
    queueName: str
    def __init__(self, queueName: _Optional[str] = ...) -> None: ...

class ConsumeMessageResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: MessageType
    def __init__(self, response: _Optional[_Union[MessageType, _Mapping]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
