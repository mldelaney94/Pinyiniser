# Pinyiniser

[![PyPI version](https://img.shields.io/pypi/v/pinyiniser)](https://pypi.org/project/pinyiniser/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A Python library that adds pinyin to Chinese strings (utf-8) using [Jieba](https://github.com/fxsjy/jieba) for word segmentation and [CC-CEDICT](https://cc-cedict.org/wiki/) for pinyin lookup.

## Installation

```
pip install pinyiniser
```

## Quick Example

```python
import pinyiniser as pyer

# Load the dictionary (True = numeral tones, False = diacritic tones)
zh_dict = pyer.get_dictionary(True)

# Add pinyin to a Chinese string
result = pyer.add_pinyin('你好，世界！', zh_dict)
print(result)
# 你好，世界！
# ni3 hao3，shi4 jie4！

# Get just the pinyin as a list
pinyin = pyer.get_pinyin('你好，世界！', zh_dict)
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']

# Use the special parameter for custom mappings (e.g. names)
special = {'卡妮雅': 'Ka3ni1ya3'}
result = pyer.add_pinyin('卡妮雅', zh_dict, special=special)
print(result)
# 卡妮雅
# Ka3ni1ya3
```

## Setup

`import pinyiniser as pyer`

## pyer.add_pinyin(zh_string, zh_dict, special={}, do_not_parse=do_not_parse_set)

Adds Pinyin to a utf-8 Chinese string.<br/>
Returns `string + \n + pinyin + \n`

### special

A dictionary of strings like:

```python
{
    '卡妮雅': 'Ka3ni1ya3',
    '伊雷米': 'Yi1lei3mi3',
    '乌蕾妮': 'Wu1lei3ni1',
}
```

It will search for the keys and output the value of the kvp.
This is a 1:1 mapping, if the string doesn't match the left hand side exactly, it will not match.
This could be more than just a way to map names, any string can be wholly replaced using this method.

### do_not_parse

`do_not_parse` is a set that by default looks like so:

```python
do_not_parse_set = {
    # Chinese special chars
    '？', '，', '！', '。', '；', '"', '"', '：', '–', '—', '＊',
    '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
    '％', '·', ''', ''', '……', '【', '】',
    # Standard special chars
    '`', '~', '!', '@', '#', '^', '&', '*', '(', ')', '-', '_',
    '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.',
    '>', '/', '?',
    # Maths
    '=', '+', '-', '/', '%',
    # Currency chars
    '$', '￥', '£', '€',
}
```

`Jieba` returns a list of words that it has detected. For English words or punctuation, they are returned as well
as an entry in the list.

We cut up the sentence using Jieba to generate a list of characters, we then step through this list
and add the pinyin to the sentence.

We need to add spaces between the elements of the list when they are added to the sentence,
but if it is in `do_not_parse` it will be added without a space, as punctuation should be.

I.e. `['ni3hao3', '.']`, if we don't use this `do_not_parse` set, becomes:
`'ni3hao3 .'`, with the set: `'ni3hao3.'`

So in order to extend this, you can create your own `do_not_parse_set` (called whatever you like) and union it
with the original `do_not_parse_set`.

```python
my_do_not_parse_set = my_do_not_parse_set.union(pyer.do_not_parse_set)
```

### zh_dict

```python
zh_dict = pyer.get_dictionary(True)
```

`True` for numerals — shuo1<br/>
`False` for diacritics — shuō

Numerals are useful for language learning as they force you to recall the tones, while diacritics are more
natural to read. Choose whichever suits your application.

#### zh_dict details

`zh_dict` is a dictionary of dictionaries, where the first key is the
character, and the second key is `'pinyin'` e.g. `zh_dict[zh_char]['pinyin']`

Any dictionary that has this set of kvp's will work, allowing you flexibility in
what you use, so you can have a dict with English too
`zh_dict[zh_char]['english']`
for further processing.

## pyer.get_pinyin(zh_string, zh_dict, do_not_parse=do_not_parse_set)

Gets pinyin as a list.

`zh_string` is just any utf-8 string of Chinese characters.

## Dependencies

- [Jieba](https://github.com/fxsjy/jieba) (>= 0.42.1) — Chinese text segmentation

## Attribution

This project uses dictionary data derived from [CC-CEDICT](https://cc-cedict.org/wiki/),
licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
