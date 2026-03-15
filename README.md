# Pinyiniser

[![PyPI version](https://img.shields.io/pypi/v/pinyiniser)](https://pypi.org/project/pinyiniser/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A Python library that converts Chinese strings (UTF-8) to pinyin using [rjieba](https://github.com/messense/rjieba) for word segmentation and [CC-CEDICT](https://cc-cedict.org/wiki/) for pinyin lookup.

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

# Get word segments and pinyin together
segments, pinyin = pyer.get_segments_and_pinyin('你好，世界！', zh_dict)
print(segments)
# ['你好', '，', '世界', '！']
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']
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

Any dictionary that has this structure will work, allowing you flexibility in
what you use — for example, you could add English definitions:
`zh_dict[zh_char]['english']`

### pyer.get_pinyin(zh_string, zh_dict, punctuation=special_tokens)

Returns pinyin as a flat list. Punctuation is preserved in place.

```python
pinyin = pyer.get_pinyin('你好，世界！', zh_dict)
# ['ni3hao3', '，', 'shi4jie4', '！']
```

### pyer.get_segments_and_pinyin(zh_string, zh_dict, punctuation=special_tokens)

Returns a tuple of `(segments, pinyin)`, both `list[str]`:
- `segments` — the word-level tokens as segmented by rjieba, with punctuation preserved as individual elements.
- `pinyin` — a list of pinyin strings, one per segment.

```python
segments, pinyin = pyer.get_segments_and_pinyin('你好，世界！', zh_dict)
print(segments)
# ['你好', '，', '世界', '！']
print(pinyin)
# ['ni3hao3', '，', 'shi4jie4', '！']
```

### punctuation / special_tokens

Both `get_pinyin` and `get_segments_and_pinyin` accept a `punctuation` parameter. This is a set of characters that are split on and passed through as-is rather than being looked up in the dictionary.

The default set (`pyer.special_tokens`) includes Chinese punctuation, standard ASCII punctuation, maths operators, and currency symbols.

To extend the default set, union your own set with the built-in one:

```python
my_punctuation = pyer.special_tokens | {'†', '‡'}
pinyin = pyer.get_pinyin('你好', zh_dict, punctuation=my_punctuation)
```

## Dependencies

- [rjieba](https://github.com/messense/rjieba) (>= 0.2.0) — Chinese text segmentation (Rust implementation of Jieba)

## Attribution

This project uses dictionary data derived from [CC-CEDICT](https://cc-cedict.org/wiki/),
licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
