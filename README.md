#Setup

import pinyiniser as pyer

##pyer.add_pinyin(string, dict, special, do_not_parse)

###special
special a dictionary of strings like:

    `{
        '卡妮雅': 'Ka3ni1ya3',
        '伊雷米': 'Yi1lei3mi3',
        '乌蕾妮': 'Wu1lei3ni1',
    }`

It will search for those strings and output the pinyin that you desire
This is a 1:1 mapping, if the string doesn't match the left hand side exactly, it will not match

###do_not_parse
do_not_parse is a dictionary that default looks like so:


`do_not_parse_set = {'？', '，', '！', '。', '；', '“', '”', '：', '–', '—', '＊',
        '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
        '％', '·', '<', '>', '’', '‘', '+', '/', '~', '!', '@', '#', '$',
        '%', '^', '&', '*', '(', ')', '_', '-', '=', '\\', '{', '}', '|', ';',
        '\'', '"', ',', '.'}`

Jieba returns a list of words that it has detected, for english words or punctuation, they are returned as well
as an entry in the list.

We cut up the sentence using jieba to generate a list of characters, we then step through this list
and add the pinyin to the sentence

we need to add spaces between the elements of the list when they are added to the sentence,
but if it is in do_not_parse it will be added without a space, as punctuation should be

i.e. ['ni3hao3', '.'], if we don't use this do_not_parse set, becomes:
'ni3hao3 .', with the set: 'ni3hao3.'

so in order to extend this, you can create your own do_not_parse_set (called whatever you like) and union it
with the original do_not_parse_set

`my_do_not_parse_set = my_do_not_parse_set.union(pyer.do_not_parse_set)`

###dict

`zh_dict = pyer.get_dictionary(True)`

True for numerals
False for diacritics
