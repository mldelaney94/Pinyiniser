import jieba
from materials import cc_cedict_parser_opt
import re

def write_lines(lines, path):
    with open(path, 'w+') as f:
        i = 0
        for line in lines:
            f.write('Line: ' + i + '\n')
            f.write(line)
        
def add_pinyin(zh_string, zh_dict, special_pinyin={}, do_not_parse={}):
    if zh_string in special_pinyin:
        return zh_string + '\n' + special_pinyin[zh_string]
    
    pinyin = get_pinyin(zh_string, zh_dict)
    zh_string += '\n'
    for item in pinyin:
        if item in do_not_parse:
            zh_string += item
        else:
            zh_string += ' ' + item

    return zh_string

def get_pinyin(zh_string, zh_dict):
    line = tuple(jieba.cut(zh_string, cut_all=False))
    pinyin = []
    for word in line:
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

def get_dictionary(numeric=False):
    if numeric == True:
        return zh_dict = parse_dict('materials/cedict_ts_no_space_numerals.u8') 
    return zh_dict = parse_dict('materials/cedict_ts_pinyin.u8')

def parse_dict(path):
    return cc_cedict_parser_opt.parse_dict(path)

if __name__ == '__name__':
    lines = []
    main(lines, False)
