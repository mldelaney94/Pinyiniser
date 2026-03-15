import rjieba
import re
from pathlib import Path

curr_dir = Path(__file__).parent
numeric_dict = curr_dir / 'data' / 'cedict_ts_numerals.u8'
diacritic_dict = curr_dir / 'data' / 'cedict_ts_diacritics.u8'

special_tokens = {
  #Chinese special chars
  '？', '，', '！', '。', '；', '“', '”', '：', '–', '—', '＊',
  '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
  '％', '·', '’', '‘', '……', '【', '】',
  #Standard special chars
  '`', '~', '!', '@', '#', '^', '&', '*', '(', ')', '-', '_',
  '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.',
  '>', '/', '?',
  #Maths
  '=', '+', '-', '/', '%',
  #Currency chars
  '$', '￥', '£', '€'
}

# Precompiled regex and sorted list for the default special_tokens
_sorted_special_tokens = sorted(special_tokens, key=len, reverse=True)
_special_tokens_pattern = re.compile(
  f"({'|'.join(re.escape(item) for item in _sorted_special_tokens)})"
)

# returns a tuple, the result of calling rjieba on the string,
# and the result of parsing that result through a dictionary,
# word by word, to get the pinyin
def get_segments_and_pinyin(
  zh_string,
  zh_dict,
  punctuation=None
) -> tuple[list[str], list[str]]:
  if punctuation is None:
    punctuation = special_tokens
  sentence_splits = split_on_punctuation(zh_string, punctuation)

  token_collection = []
  pinyin = []
  for fragment in sentence_splits:
    if fragment not in punctuation:
      tokens = tuple(rjieba.cut(fragment))
      token_collection.extend(tokens)
      pinyin.extend(get_pinyin_for_tokens(tokens, zh_dict, punctuation))
    else:
      token_collection.append(fragment)
      pinyin.append(fragment)

  return ( token_collection, pinyin )

def get_pinyin(zh_string,
  zh_dict,
  punctuation=None
) -> list[str]:
  _, pinyin = get_segments_and_pinyin(zh_string, zh_dict, punctuation)
  return pinyin

def get_pinyin_for_tokens(
  tokens,
  zh_dict,
  punctuation
) -> list[str]:
  pinyin = []
  for token in tokens:
    if token in zh_dict:
      pinyin.append(zh_dict[token]['pinyin'])
    elif token in punctuation or ord(token[0]) < 255:
      pinyin.append(token)
    else: 
      for character in token:
        if character in zh_dict:
          pinyin.append(zh_dict[character]['pinyin'])
        else:
          pinyin.append(character)

  return pinyin

def split_on_punctuation(zh_string, punctuation=special_tokens):
  if punctuation is special_tokens:
    split_string = _special_tokens_pattern.split(zh_string)
  else:
    length_sorted_punctuation = sorted(punctuation, key=len, reverse=True)
    escaped_punctuation = [re.escape(item) for item in length_sorted_punctuation]
    split_string = re.split(f"({'|'.join(escaped_punctuation)})", zh_string)

  # re.split produces empty strings if two pieces of punctuation are next to each other
  return [s for s in split_string if s]

def get_dictionary(numeric=True):
  if not numeric:
    return parse_dict(diacritic_dict)
  return parse_dict(numeric_dict)

def parse_dict(path):
  return cc_cedict_parser.parse_dict(path)

if __name__ == '__main__':
  from data import cc_cedict_parser
else:
  from .data import cc_cedict_parser
