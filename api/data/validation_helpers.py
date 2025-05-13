# validators.py
import re
from typing import List, Union

from api.constants import NAME_REGEX, ASSET_LINK_REGEX, ALPHA_NUMERIC_REGEX, ESF_WIKI_LINK_REGEX

def validate_uid_string(value: str) -> bool:
    return re.fullmatch(ALPHA_NUMERIC_REGEX, value)

def validate_name_string(value: str) -> bool:
    return re.fullmatch(NAME_REGEX, value)

def validate_asset_url_string(value: str) -> bool:
    return re.fullmatch(ASSET_LINK_REGEX, value)

def validate_wiki_url_string(value: str) -> bool:
    return re.fullmatch(ESF_WIKI_LINK_REGEX, value)

def is_negative(num: List[Union[int, float]]) -> bool:
    return  num < 0
