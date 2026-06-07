"""Builds a dictionary of character to pinyin

  Access by:
  [character]['pinyin']

This leaves things flexible if want to have the English definition
too
"""
from __future__ import annotations

from os import PathLike
from pathlib import Path
from typing import Literal

from ..types import ZhDict, ZhEntry, ZhParts

def parse_dict(path: Path | PathLike[str]) -> ZhDict:
  #make each line into a dictionary
  with open(path, 'r') as f:
    lines = f.readlines()
    return parse_lines(lines)

def parse_lines(lines: list[str]) -> ZhDict:
  dictionary: ZhDict = {}
  for line in lines:
    parts = get_parts_of_line(line)
    add_entry(parts, dictionary)

  return dictionary

def get_parts_of_line(line: str) -> ZhParts | Literal['']:
  parts: ZhParts = {}
  chinese, english = line.split('/', 1)
  if chinese in skip:
    return ''
  trad, simp, pinyin = chinese.split(' ', 2)
  pinyin = prep_pinyin(pinyin)

  is_rare = False
  for marker in rare_markers:
    if marker in english:
      is_rare = True
      break

  entry: ZhEntry = {'pinyin': pinyin, 'is_rare': is_rare}
  parts[simp.strip()] = entry
  parts[trad.strip()] = entry

  return parts

def prep_pinyin(pinyin: str) -> str:
  return pinyin.strip('[] ').lower()

#mutate dictionary in place
def add_entry(parts: ZhParts | Literal[''], dictionary: ZhDict) -> None:
  for key in parts:
    if key not in dictionary or dictionary[key]['is_rare'] is True:
      dictionary[key] = parts[key]

if __name__ == "__main__":
  from pinyin_skip import skip
  from pinyin_skip import rare_markers
else:
  from .pinyin_skip import skip
  from .pinyin_skip import rare_markers
