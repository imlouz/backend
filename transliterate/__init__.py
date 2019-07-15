# misc
from enum import Enum


class Direction(str, Enum):
    lat2cyr = "lat2cyr"
    cyr2lat = "cyr2lat"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


async def lat2cyr(content: str) -> str:
    return "foobar"
