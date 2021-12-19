from pinyin_skip import skip

def numerals_to_diacritics ():
    with open('cedict_ts_numerals.u8', 'r') as f:
        with open('cedict_ts_pinyin.u8', 'w+') as g:
            for line in f:
                chinese, english = line.split('/', 1)
                if chinese in skip:
                    continue
                trad, simp, pinyin = chinese.split(' ', 2)
                pinyin = prep_pinyin(pinyin)

                i = 0
                while i < len(pinyin):
                    for key in numeral_to_diacritic:
                        if key in pinyin[i]:
                            pinyin[i] = pinyin[i].replace(key, numeral_to_diacritic[key])
                            break
                    i += 1

                g.write(trad + ' ' + simp + ' [' + ''.join(pinyin) + '] /' +
                        english)

def prep_pinyin(pinyin):
    return pinyin.strip('[] ').lower().split(' ')

numeral_to_diacritic = {
        'iang1': 'iāng', 'iang2': 'iáng', 'iang3': 'iǎng', 'iang4': 'iàng', 'iang5': 'iang',
        'uang1': 'uāng', 'uang2': 'uáng', 'uang3': 'uǎng', 'uang4': 'uàng', 'uang5': 'uang',
        'iong1': 'iōng', 'iong2': 'ióng', 'iong3': 'iǒng', 'iong4': 'iòng', 'iong5': 'iong',
        'ong1': 'ōng', 'ong2': 'óng', 'ong3': 'ǒng', 'ong4': 'òng', 'ong5': 'ong',
        'eng1': 'ēng', 'eng2': 'éng', 'eng3': 'ěng', 'eng4': 'èng', 'eng5': 'eng',
        'ing1': 'īng', 'ing2': 'íng', 'ing3': 'ǐng', 'ing4': 'ìng', 'ing5': 'ing',
        'ang1': 'āng', 'ang2': 'áng', 'ang3': 'ǎng', 'ang4': 'àng', 'ang5': 'ang',
        'iao1': 'iāo', 'iao2': 'iáo', 'iao3': 'iǎo', 'iao4': 'iào', 'iao5': 'iao',
        'ian1': 'iān', 'ian2': 'ián', 'ian3': 'iǎn', 'ian4': 'iàn', 'ian5': 'ian',
        'uai1': 'uāi', 'uai2': 'uái', 'uai3': 'uǎi', 'uai4': 'uài', 'uai5': 'uai',
        'uan1': 'uān', 'uan2': 'uán', 'uan3': 'uǎn', 'uan4': 'uàn', 'uan5': 'uan',
        'en1': 'ēn', 'en2': 'én', 'en3': 'ěn', 'en4': 'èn', 'en5': 'en',
        'er1': 'ēr', 'er2': 'ér', 'er3': 'ěr', 'er4': 'èr', 'er5': 'er',
        'ei1': 'ēi', 'ei2': 'éi', 'ei3': 'ěi', 'ei4': 'èi', 'ei5': 'ei',
        'ie1': 'iē', 'ie2': 'ié', 'ie3': 'iě', 'ie4': 'iè', 'ie5': 'ie',
        'ue1': 'uē', 'ue2': 'ué', 'ue3': 'uě', 'ue4': 'uè', 'ue5': 'ue',
        'ua1': 'uā', 'ua2': 'uá', 'ua3': 'uǎ', 'ua4': 'uà', 'ua5': 'ua',
        'ia1': 'iā', 'ia2': 'iá', 'ia3': 'iǎ', 'ia4': 'ià', 'ia5': 'ia',
        'ai1': 'āi', 'ai2': 'ái', 'ai3': 'ǎi', 'ai4': 'ài', 'ai5': 'ai',
        'ao1': 'āo', 'ao2': 'áo', 'ao3': 'ǎo', 'ao4': 'ào', 'ao5': 'ao',
        'an1': 'ān', 'an2': 'án', 'an3': 'ǎn', 'an4': 'àn', 'an5': 'an',
        'un1': 'ūn', 'un2': 'ún', 'un3': 'ǔn', 'un4': 'ùn', 'un5': 'un',
        'iu1': 'iū', 'iu2': 'iú', 'iu3': 'iǔ', 'iu4': 'iù', 'iu5': 'iu',
        'ui1': 'uī', 'ui2': 'uí', 'ui3': 'uǐ', 'ui4': 'uì', 'ui5': 'ui',
        'in1': 'īn', 'in2': 'ín', 'in3': 'ǐn', 'in4': 'ìn', 'in5': 'in',
        'uo1': 'uō', 'uo2': 'uó', 'uo3': 'uǒ', 'uo4': 'uò', 'uo5': 'uo',
        'ou1': 'ōu', 'ou2': 'óu', 'ou3': 'ǒu', 'ou4': 'òu', 'ou5': 'ou',
        'u:e1': 'üē', 'u:e2': 'üé', 'u:e3': 'üě', 'u:e4': 'üè', 'u:e5': 'üe',
        'i1': 'ī', 'i2': 'í', 'i3': 'ǐ', 'i4': 'ì', 'i5': 'i',
        'a1': 'ā', 'a2': 'á', 'a3': 'ǎ', 'a4': 'à', 'a5': 'a',
        'e1': 'ē', 'e2': 'é', 'e3': 'ě', 'e4': 'è', 'e5': 'e',
        'o1': 'ō', 'o2': 'ó', 'o3': 'ǒ', 'o4': 'ò', 'o5': 'o',
        'u1': 'ū', 'u2': 'ú', 'u3': 'ǔ', 'u4': 'ù', 'u5': 'u',
        'u:1': 'ǖ', 'u:2': 'ǘ', 'u:3': 'ǚ', 'u:4': 'ǜ', 'u:5': 'ü'
        }

if __name__ == '__main__':
    numerals_to_diacritics()
