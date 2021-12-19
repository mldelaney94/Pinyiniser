from pinyin_skip import skip

def numerals_to_diacritics ():
    with open('cedict_ts_numerals.u8', 'r') as f:
        with open('cedict_ts_no_space_numerals.u8', 'w+') as g:
            for line in f:
                chinese, english = line.split('/', 1)
                if chinese in skip:
                    continue
                trad, simp, pinyin = chinese.split(' ', 2)
                pinyin = prep_pinyin(pinyin)

                g.write(trad + ' ' + simp + ' [' + ''.join(pinyin) + '] /' +
                        english)

def prep_pinyin(pinyin):
    return pinyin.strip('[] ').lower().split(' ')

if __name__ == '__main__':
    numerals_to_diacritics()
