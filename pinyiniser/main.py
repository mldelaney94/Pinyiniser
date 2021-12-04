import jieba
import re
from .materials import cc_cedict_parser_opt

do_not_parse_set = {'？', '，', '！', '。', '；', '“', '”', '：', '–', '—', '＊',
        '…', '、', '～', '－', '（', '）', '─', '＜', '＞', '．', '《', '》',
        '％', '·', '>', '’'}

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
        
def add_pinyin(zh_string, zh_dict, special_pinyin={},
        do_not_parse=do_not_parse_set):
    if zh_string in special_pinyin:
        return zh_string + '\n' + special_pinyin[zh_string] + '\n'
    
    pinyin = get_pinyin(zh_string, zh_dict)
    zh_string += '\n'
    first = True 
    for item in pinyin:
        if item in do_not_parse or first:
            zh_string += item
            first = False
        else:
            zh_string += ' ' + item

    return zh_string + '\n'

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
        return parse_dict('./materials/cedict_ts_no_space_numerals.u8') 
    return parse_dict('./materials/cedict_ts_pinyin.u8')

def parse_dict(path):
    return cc_cedict_parser_opt.parse_dict(path)

if __name__ == '__main__':
    ace = read_lines('testwrite.txt')
