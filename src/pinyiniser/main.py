import jieba
import pinyiniser
import os
from pathlib import Path

curr_dir = '\\'.join(pinyiniser.__file__.split('\\')[0:-1])
numeric_dict = os.path.join(curr_dir, Path('./data/cedict_ts_numerals.u8'))
diacritic_dict = os.path.join(curr_dir, Path('./data/cedict_ts_diacritics.u8'))

do_not_parse_set = {
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

def write_lines(lines, path):
  with open(path, 'w+') as f:
    i = 1
    for line in lines:
      f.write('Line ' + str(i) + ':\n')
      f.write(line)
      i += 1
    f.write('Line ' + str(i) + ':\n')

def read_lines(path):
  with open(path, 'r') as f:
    lines = []
    string_to_add = ''
    first = True
    for line in f.readlines():
      if 'Line' in line:
        if first:
          first = False
          continue
        lines.append(string_to_add)
        string_to_add = ''
      else:
        string_to_add += line
  return lines

# returns a tuple, the zh_string, and the pinyin string
# the zh_string will be augmented with non-breaking spaces
# around the chinese words
def get_segments_and_pinyin(zh_string, zh_dict, do_not_parse=do_not_parse_set):
  line_segs = tuple(jieba.cut(zh_string, cut_all=False))

  pinyin = []
  for word in line_segs:
    if word in zh_dict:
      pinyin.append(zh_dict[word]['pinyin'])
    else:
      if word in do_not_parse or ord(word[0]) < 255:
        pinyin.append(word)
      else: 
        for character in word:
          if character in zh_dict:
            pinyin.append(zh_dict[character]['pinyin'])
          else:
            pinyin.append(character)

  return ( line_segs.join('\u200B'), pinyin )


def get_pinyin(zh_string, zh_dict, do_not_parse=do_not_parse_set):
  line_segs = tuple(jieba.cut(zh_string, cut_all=False))
  pinyin = []
  for word in line_segs:
    if word in zh_dict:
      pinyin.append(zh_dict[word]['pinyin'])
    else:
      if word in do_not_parse or ord(word[0]) < 255:
        pinyin.append(word)
      else: 
        for character in word:
          if character in zh_dict:
            pinyin.append(zh_dict[character]['pinyin'])
          else:
            pinyin.append(character)

    return pinyin

def get_dictionary(numeric=True):
  if numeric == False:
    return parse_dict(diacritic_dict)
  return parse_dict(numeric_dict)

def parse_dict(path):
  return cc_cedict_parser.parse_dict(path)

if __name__ == '__main__':
  from data import cc_cedict_parser
else:
  from .data import cc_cedict_parser
