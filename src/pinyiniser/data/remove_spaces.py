from __future__ import annotations

# Turn
# 挪威 挪威 [Nuo2 wei1] /Norway/
# into
# 挪威 挪威 [nuo2wei1] /Norway/
def remove_spaces_from_pinyin() -> None:
  with open('cedict_ts.u8', 'r') as f:
    with open('cedict_ts_numerals.u8', 'w+') as g:
      for line in f:
        chinese, english = line.split('/', 1)

        trad, simp, pinyin = chinese.split(' ', 2)
        pinyin = prep_pinyin(pinyin)

        g.write(trad + ' ' + simp + ' [' + ''.join(pinyin) + '] /' +
        english)

def prep_pinyin(pinyin: str) -> list[str]:
  return pinyin.strip('[] ').lower().split(' ')

if __name__ == '__main__':
  remove_spaces_from_pinyin()
