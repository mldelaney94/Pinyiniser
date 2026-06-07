from __future__ import annotations

from typing import TypeAlias, TypedDict

ChineseCharacter: TypeAlias = str

class ZhEntry(TypedDict):
  pinyin: str
  is_rare: bool

ZhDict = dict[ChineseCharacter, ZhEntry]
ZhParts = dict[ChineseCharacter, ZhEntry]
