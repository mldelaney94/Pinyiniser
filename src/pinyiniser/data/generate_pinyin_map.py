"""Generates a complete pinyin numeral-to-diacritic lookup dictionary
by combining every initial with every final, plus standalone consonant
syllables. All combinations are included, even illegal ones.

Result is written to pinyin_map.py.
"""

initials = [
  '', 'b', 'p', 'm', 'f',
  'd', 't', 'n', 'l',
  'g', 'k', 'h',
  'j', 'q', 'x',
  'zh', 'ch', 'sh', 'r',
  'z', 'c', 's',
  'y', 'w',
]

finals = {
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
  'u:1': 'ǖ', 'u:2': 'ǘ', 'u:3': 'ǚ', 'u:4': 'ǜ', 'u:5': 'ü',
}

# Standalone consonant syllables (interjections, erhua, etc.)
# The combining mark goes on the tone-bearing consonant:
#   (prefix, tone_bearer, suffix)
# e.g. 'ng' → mark on 'n', then 'g' after
standalone_shapes = {
  'm':   ('', 'm', ''),
  'n':   ('', 'n', ''),
  'r':   ('', 'r', ''),
  'ng':  ('', 'n', 'g'),
  'hm':  ('h', 'm', ''),
  'hng': ('h', 'n', 'g'),
}

combining_marks = {
  '1': '\u0304',  # macron  ̄
  '2': '\u0301',  # acute   ́
  '3': '\u030C',  # caron   ̌
  '4': '\u0300',  # grave   ̀
  '5': '',         # neutral
}


def generate():
  pinyin_map = {}

  for initial in initials:
    for numeral_final, diacritic_final in finals.items():
      pinyin_map[initial + numeral_final] = initial + diacritic_final

  for consonant, (prefix, bearer, suffix) in standalone_shapes.items():
    for tone_num, mark in combining_marks.items():
      pinyin_map[consonant + tone_num] = prefix + bearer + mark + suffix

  with open('pinyin_map.py', 'w', encoding='utf-8') as f:
    f.write('pinyin_map = {\n')
    for key in sorted(pinyin_map):
      f.write(f"  '{key}': '{pinyin_map[key]}',\n")
    f.write('}\n')

  print(f'Wrote {len(pinyin_map)} entries to pinyin_map.py')


if __name__ == '__main__':
  generate()
