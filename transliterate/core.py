# charmap
from .charmap import lat2cyr_charmap

# misc
import enum
import re


class Direction(str, enum.Enum):
    lat2cyr = "lat2cyr"
    cyr2lat = "cyr2lat"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


async def lat2cyr(content: str) -> str:
    text = content

    for src, dst in lat2cyr_charmap.items():
        text = re.sub(src, dst, text)

    return text
