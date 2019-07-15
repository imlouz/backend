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
    charmap = {
        r"ye": r"е",
        r"ya": r"я",
        r"yu": r"ю",
        r"yo": r"ё",
        r"o‘": r"ў",
        r"o'": r"ў",
        r"ch": r"ч",
        r"sh": r"ш",
        r"Sh": r"Ш",
        r"yev+": r"ев",
        r"o‘": r"ў",
        r"O‘": r"Ў",
        r"g‘": r"ғ",
        r"G‘": r"Ғ",
        r"a": r"а",
        r"b": r"б",
        r"c": r"ц",
        r"d": r"д",
        r"\se": r" э",
        r"f": r"ф",
        r"g": r"г",
        r"h": r"ҳ",
        r"i": r"и",
        r"j": r"ж",
        r"k": r"к",
        r"l": r"л",
        r"m": r"м",
        r"n": r"н",
        r"o": r"о",
        r"p": r"п",
        r"q": r"қ",
        r"r": r"р",
        r"s": r"с",
        r"t": r"т",
        r"u": r"у",
        r"v": r"в",
        r"x": r"х",
        r"y": r"й",
        r"z": r"з",
        r"A": r"А",
        r"B": r"Б",
        r"C": r"Ц",
        r"D": r"Д",
        r"E": r"Э",
        r"F": r"Ф",
        r"G": r"Г",
        r"H": r"Ҳ",
        r"I": r"И",
        r"J": r"Ж",
        r"K": r"К",
        r"L": r"Л",
        r"M": r"М",
        r"N": r"Н",
        r"O": r"О",
        r"P": r"П",
        r"Q": r"Қ",
        r"R": r"Р",
        r"S": r"С",
        r"T": r"Т",
        r"U": r"У",
        r"V": r"В",
        r"X": r"Х",
        r"Y": r"Й",
        r"Z": r"З",
        r"'": r"ъ",
    }
    text = content

    for src, dst in charmap.items():
        text = re.sub(src, dst, text)

    return text
