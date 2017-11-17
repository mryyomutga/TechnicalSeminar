# -*- coding: utf-8 -*-
# 正規表現
import re
pat = r"\d+"
str = "This pen is 100yen."
re.search(pat, str)
print(str)

words = ["orange", "october", "octpus",
         "order", "banana", "baby", "busy"
         ]

pattern = r"oc.*"
print("ocで始まるパターン =", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

pattern = r"b.*y"
print("bで始まりyで終わるパターン =", pattern)
for word in words:
    if re.match(pattern, word):
        print("-", word)

# ^で先頭、$で末尾
print(re.search(r"^abc$", "abc"))
print(re.search(r"^abc$", "abcd"))
print(re.search(r"^abc$", "xabc"))

pat = r"\.png$"
print(re.search(pat, "abc.png"))
print(re.search(pat, "abc.png-doc.txt"))

# .で任意の一文字
words = ["soy", "soup", "nuts", "spot"]
pat = r"^s...$"
s = [i for i in words if re.search(pat, i)]
print(s)

print(re.search(r"ba*", "b"))
print(re.search(r"ba+", "baaaaaaaa"))
# {m,n}でm回以上n回以下
print(re.search(r"ba{1,3}", "baaaaaaaa"))

# 最小単位の繰り返し
s = "青巻紙赤巻紙黄巻紙"
print(re.findall(r".+紙", s))
print(re.findall(r".+?紙", s))

# 文字集合
# パターンのコンパイル
zipre = re.compile(r"^[0-9]{3}\-[0-9]{4}$")
print(zipre.search("440-0012"))
print(zipre.search("1111-2222"))

# 単語の選択
s = "I like red color."
pat = r"\w+ (color|colour)"
print(re.search(pat, s))

s = "date: 2017/11/16"
pat = r"(\d{4})/(\d{1,2})/(\d{1,2})"
g = re.search(pat, s)
print(g.groups())
