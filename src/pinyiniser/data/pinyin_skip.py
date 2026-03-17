"""For all those words that have multiple pronunciations, we remove the rarer
one"""

skip = {'說 说 [shui4] ',
        '打 打 [da2] ',
        '嗎 吗 [ma2] ',
        '么 幺 [yao1] ',
        '都 都 [du1] '}

rare_markers = {
  "surname",
  "(archaic)",
  "variant of",
  "old variant of",
  "used in",
  "(literary)",
  "(dialect)",
  "(bound form)"
}
