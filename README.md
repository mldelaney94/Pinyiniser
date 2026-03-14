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

# Get pinyin as a list
pinyin = pyer.get_pinyin('你好，世界！', zh_dict)
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']

# Get segmented text (with zero-width spaces at word boundaries) and pinyin
segmented, pinyin = pyer.get_segments_and_pinyin('你好，世界！', zh_dict)
print(repr(segmented))
# '你好\u200b，\u200b世界\u200b！'
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']
```

## Setup

```python
import pinyiniser as pyer
```

## API

### pyer.get_dictionary(numeric=True)

Loads the CC-CEDICT pinyin dictionary.

```python
zh_dict = pyer.get_dictionary(True)
```

`True` for numerals e.g. shuo1<br/>
`False` for diacritics e.g. shuō

Numerals are useful for language learning as they introduce friction to reading solely pinyin,
while diacritics are more natural to read and more professional.
Choose whichever suits your application.

#### zh_dict details

`zh_dict` is a dictionary of dictionaries, where the first key is the
character, and the second key is `'pinyin'` e.g. `zh_dict[zh_char]['pinyin']`

Any dictionary that has this set of kvp's will work, allowing you flexibility in
what you use, so you can have a dict with English too
`zh_dict[zh_char]['english']`
for further processing.

### pyer.get_pinyin(zh_string, zh_dict, do_not_parse=do_not_parse_set)

Gets pinyin as a list.

`zh_string` is any utf-8 string of Chinese characters.

```python
pinyin = pyer.get_pinyin('你好，世界！', zh_dict)
# ['ni3hao3', '，', 'shi4jie4', '！']
```

### pyer.segment_with_pinyin(zh_string, zh_dict, do_not_parse=do_not_parse_set)

Segments the Chinese string at word boundaries and returns both the segmented text and the pinyin.

Returns a tuple of `(segmented_text, pinyin_list)`:
- `segmented_text` — the original string with zero-width spaces (`\u200B`) inserted between word boundaries (as detected by Jieba). This is useful for rendering Chinese text with visible word groupings without altering the visual appearance.
- `pinyin_list` — a list of pinyin strings, one per segment (same as `get_pinyin`).

```python
segmented, pinyin = pyer.segment_with_pinyin('你好，世界！', zh_dict)
print(repr(segmented))
# '你好\u200b，\u200b世界\u200b！'
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']
```

### do_not_parse

Both `get_pinyin` and `segment_with_pinyin` accept a `do_not_parse` parameter. This is a set of characters (punctuation, symbols) that should not have spaces inserted around them in the pinyin output.

The default set includes:

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

Jieba returns a list of segmented words. For English words or punctuation, they are returned as entries in the list too. We need to add spaces between pinyin elements, but punctuation should be attached without a space.

I.e. `['ni3hao3', '.']` — without `do_not_parse`, becomes `'ni3hao3 .'`; with it: `'ni3hao3.'`

To extend the default set, union your own set with the built-in one:

```python
my_do_not_parse_set = my_do_not_parse_set.union(pyer.do_not_parse_set)
```

## Dependencies

- [Jieba](https://github.com/fxsjy/jieba) (>= 0.42.1) — Chinese text segmentation

## Attribution

This project uses dictionary data derived from [CC-CEDICT](https://cc-cedict.org/wiki/),
licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
