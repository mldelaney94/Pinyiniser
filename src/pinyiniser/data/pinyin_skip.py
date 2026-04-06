"""For all those words that have multiple pronunciations, we remove the rarer
one"""

skip = {'說 说 [shui4] ',
        '打 打 [da2] ',
        '嗎 吗 [ma2] ',
        '么 幺 [yao1] ',
        '這 这 [zhèi] ',
        '會 会 [kuai4] ',
        '看 看 [kan1] ',
        '都 都 [du1] ',
        '這 这 [zhei4] ',
        '着 着 [zhuo2] '}

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
