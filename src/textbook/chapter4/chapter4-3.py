# -*- coding: utf-8 -*-
# ファイル処理
# ファイル読み込み
a_file = open("mt7_7.txt", encoding="utf-8")
s = a_file.read()
a_file.close()
print(s)

# ファイル書き込み
a_file = open("test.txt", mode="w", encoding="utf-8")
a_file.write("私は失敗したことがない。\n")
a_file.write("ただ、一万通りの方法を\n見つけただけだ。\n")
a_file.write("- トーマス・エジソン\n")
a_file.close()

# try-finallyで確実に閉じる
a_file = open("test.txt", mode="w", encoding="utf-8")
try:
    a_file.write("私は失敗したことがない。\n")
    a_file.write("ただ、一万通りの方法を\n見つけただけだ。\n")
    a_file.write("- トーマス・エジソン\n")
finally:
    a_file.close()

# withで簡単にファイル処理を行う
# closeが自動で呼ばれる
with open("test.txt", mode="w", encoding="utf-8") as f:
    f.write("私は失敗したことがない。\n")
    f.write("ただ、一万通りの方法を\n見つけただけだ。\n")
    f.write("- トーマス・エジソン\n")

# 1行ずつ処理する
key = "find"
with open("mt7_7.txt", encoding="utf-8") as tf:
    for i, line in enumerate(tf):
        if line.find(key) >= 0:
            print(i+1, ":", line)

# オブジェクトを操作する
import json
data = {"no":5,
        "code":("jas", 1, 19),
        "scr":"be quick to listen, slow to speak, slow to anger"
        }
f_name = "test.json"
# json形式でdump
with open(f_name, "w") as fp:
    json.dump(data, fp)

# jsonファイルからload
with open(f_name, "r") as fp:
    r = json.load(fp)
    print("no =", r["no"])
    print("code =", r["code"])
    print("scr =", r["scr"])
