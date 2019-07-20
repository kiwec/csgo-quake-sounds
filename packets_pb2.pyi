# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PacketInfo(google___protobuf___message___Message):
    class Type(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> PacketInfo.Type: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[PacketInfo.Type]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, PacketInfo.Type]]: ...
        GAME_EVENT = typing___cast(PacketInfo.Type, 0)
        PLAY_SOUND = typing___cast(PacketInfo.Type, 1)
        SOUND_REQUEST = typing___cast(PacketInfo.Type, 2)
        SOUND_RESPONSE = typing___cast(PacketInfo.Type, 3)
        CLIENT_UPDATE = typing___cast(PacketInfo.Type, 4)
        SOUNDS_LIST = typing___cast(PacketInfo.Type, 5)
    GAME_EVENT = typing___cast(PacketInfo.Type, 0)
    PLAY_SOUND = typing___cast(PacketInfo.Type, 1)
    SOUND_REQUEST = typing___cast(PacketInfo.Type, 2)
    SOUND_RESPONSE = typing___cast(PacketInfo.Type, 3)
    CLIENT_UPDATE = typing___cast(PacketInfo.Type, 4)
    SOUNDS_LIST = typing___cast(PacketInfo.Type, 5)

    type = ... # type: PacketInfo.Type
    length = ... # type: int

    def __init__(self,
        *,
        type : typing___Optional[PacketInfo.Type] = None,
        length : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PacketInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"length",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"length",b"length",u"type",b"type"]) -> None: ...

class SoundRequest(google___protobuf___message___Message):
    sound_hash = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]

    def __init__(self,
        *,
        sound_hash : typing___Optional[typing___Iterable[bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SoundRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"sound_hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"sound_hash",b"sound_hash"]) -> None: ...

class SoundResponse(google___protobuf___message___Message):
    data = ... # type: bytes
    hash = ... # type: bytes

    def __init__(self,
        *,
        data : typing___Optional[bytes] = None,
        hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SoundResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"data",u"hash"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"hash",b"hash"]) -> None: ...

class GameEvent(google___protobuf___message___Message):
    class Type(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> GameEvent.Type: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[GameEvent.Type]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, GameEvent.Type]]: ...
        MVP = typing___cast(GameEvent.Type, 0)
        ROUND_WIN = typing___cast(GameEvent.Type, 1)
        ROUND_LOSE = typing___cast(GameEvent.Type, 2)
        SUICIDE = typing___cast(GameEvent.Type, 3)
        TEAMKILL = typing___cast(GameEvent.Type, 4)
        DEATH = typing___cast(GameEvent.Type, 5)
        FLASH = typing___cast(GameEvent.Type, 6)
        KNIFE = typing___cast(GameEvent.Type, 7)
        HEADSHOT = typing___cast(GameEvent.Type, 8)
        KILL = typing___cast(GameEvent.Type, 9)
        COLLATERAL = typing___cast(GameEvent.Type, 10)
        ROUND_START = typing___cast(GameEvent.Type, 11)
        TIMEOUT = typing___cast(GameEvent.Type, 12)
    MVP = typing___cast(GameEvent.Type, 0)
    ROUND_WIN = typing___cast(GameEvent.Type, 1)
    ROUND_LOSE = typing___cast(GameEvent.Type, 2)
    SUICIDE = typing___cast(GameEvent.Type, 3)
    TEAMKILL = typing___cast(GameEvent.Type, 4)
    DEATH = typing___cast(GameEvent.Type, 5)
    FLASH = typing___cast(GameEvent.Type, 6)
    KNIFE = typing___cast(GameEvent.Type, 7)
    HEADSHOT = typing___cast(GameEvent.Type, 8)
    KILL = typing___cast(GameEvent.Type, 9)
    COLLATERAL = typing___cast(GameEvent.Type, 10)
    ROUND_START = typing___cast(GameEvent.Type, 11)
    TIMEOUT = typing___cast(GameEvent.Type, 12)

    update = ... # type: GameEvent.Type
    proposed_sound_hash = ... # type: bytes
    kill_count = ... # type: int
    round = ... # type: int

    def __init__(self,
        *,
        update : typing___Optional[GameEvent.Type] = None,
        proposed_sound_hash : typing___Optional[bytes] = None,
        kill_count : typing___Optional[int] = None,
        round : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GameEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"kill_count",u"proposed_sound_hash",u"round",u"update"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"kill_count",b"kill_count",u"proposed_sound_hash",b"proposed_sound_hash",u"round",b"round",u"update",b"update"]) -> None: ...

class ClientUpdate(google___protobuf___message___Message):
    steamid = ... # type: int
    shard_code = ... # type: bytes

    def __init__(self,
        *,
        steamid : typing___Optional[int] = None,
        shard_code : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ClientUpdate: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"shard_code",u"steamid"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"shard_code",b"shard_code",u"steamid",b"steamid"]) -> None: ...

class PlaySound(google___protobuf___message___Message):
    steamid = ... # type: int
    sound_hash = ... # type: bytes

    def __init__(self,
        *,
        steamid : typing___Optional[int] = None,
        sound_hash : typing___Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PlaySound: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"sound_hash",u"steamid"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"sound_hash",b"sound_hash",u"steamid",b"steamid"]) -> None: ...
