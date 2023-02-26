import re
from typing import Dict

from .data import CODE_ALIASES, COUNTRIES

__all__ = ['code', 'flag', 'name', 'countries']
__version__ = '0.0.1'

countries = COUNTRIES  # compatibility
names_to_codes: Dict[str, str] = {}  # cache

MAGIC_NUMBER = 127397
NOT_FOUND = ''

CODE_RE = re.compile('^[a-z]{2}$', re.IGNORECASE)
NAME_RE = re.compile('^.{2,}$')
FLAG_RE = re.compile('^[🇦-🇿]{2}$', re.UNICODE)



def code(text: str) -> str:
    return _flag_to_code(text) or _name_to_code(text)


def flag(text: str) -> str:
    if text.upper() in CODE_ALIASES:
        text = CODE_ALIASES[text.upper()]

    elif CODE_RE.match(text) is None:
        text = _name_to_code(text)

    return _code_to_flag(text)


def name(text: str) -> str:
    if FLAG_RE.match(text) is not None:
        text = _flag_to_code(text)

    elif text.upper() in CODE_ALIASES:
        text = CODE_ALIASES[text.upper()]

    return _code_to_name(text)


def _get_names_to_codes() -> Dict[str, str]:
    if not names_to_codes:
        for code, country_names in COUNTRIES.items():
            for name in country_names:
                names_to_codes[name.lower()] = code
    return names_to_codes


def _fuzzy_match(one: str, another: str) -> bool:
    # Cases like:
    #    "Vatican" <-> "Holy See (Vatican City State)"
    #    "Russia"  <-> "Russian Federation"
    if one in another or another in one:
        return True

    # Cases like:
    #    "British Virgin Islands" <-> "Virgin Islands, British"
    #    "Republic of Moldova"    <-> "Moldova, Republic of"
    if ',' in another:
        reversed_name = ' '.join(reversed(another.split(', ')))
        if reversed_name in one or one in reversed_name:
            return True
    return False


def _name_to_code(name: str) -> str:
    if not name or NAME_RE.match(name) is None:
        return NOT_FOUND

    name = name.strip().lower()
    names_to_codes = _get_names_to_codes()

    # Look for exact match
    code = names_to_codes.get(name)
    if code is not None:
        return code

    # Look for inexact match
    codes = set()
    for country_name, code in names_to_codes.items():
        if _fuzzy_match(name, country_name):
            codes.add(code)

    # Return only when exactly one match was found
    #   prevents cases like "United"
    if len(codes) == 1:
        return codes.pop()

    return NOT_FOUND


def _code_to_name(code: str) -> str:
    if not code or CODE_RE.match(code) is None:
        return NOT_FOUND

    return COUNTRIES.get(code.upper(), [NOT_FOUND])[0]


def _code_to_flag(code: str) -> str:
    if not code or CODE_RE.match(code) is None:
        return NOT_FOUND

    code = code.upper()
    if code not in COUNTRIES:
        return NOT_FOUND

    return ''.join(map(lambda x: chr(ord(x) + MAGIC_NUMBER), code))


def _flag_to_code(flag: str) -> str:
    if not flag or FLAG_RE.match(flag) is None:
        return NOT_FOUND

    return ''.join(map(lambda x: chr(ord(x) - MAGIC_NUMBER), flag))
