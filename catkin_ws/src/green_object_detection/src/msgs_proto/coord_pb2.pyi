from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PointStamped(_message.Message):
    __slots__ = ["header", "point"]
    class Header(_message.Message):
        __slots__ = ["frame_id", "seq", "stamp"]
        FRAME_ID_FIELD_NUMBER: _ClassVar[int]
        SEQ_FIELD_NUMBER: _ClassVar[int]
        STAMP_FIELD_NUMBER: _ClassVar[int]
        frame_id: str
        seq: int
        stamp: int
        def __init__(self, seq: _Optional[int] = ..., stamp: _Optional[int] = ..., frame_id: _Optional[str] = ...) -> None: ...
    class Point(_message.Message):
        __slots__ = ["x", "y", "z"]
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        Z_FIELD_NUMBER: _ClassVar[int]
        x: float
        y: float
        z: float
        def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...
    HEADER_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    header: PointStamped.Header
    point: PointStamped.Point
    def __init__(self, header: _Optional[_Union[PointStamped.Header, _Mapping]] = ..., point: _Optional[_Union[PointStamped.Point, _Mapping]] = ...) -> None: ...
