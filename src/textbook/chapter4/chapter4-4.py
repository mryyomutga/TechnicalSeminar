# -*- coding: utf-8 -*-
# コマンドラインツールの作成
import sys
import os
# コマンドライン引数の確認
# for i, v in enumerate(sys.argv):
#     print(i, v)

if len(sys.argv) <= 1:
    print("[USAGE] findtext (keyword)")
    sys.exit(0)

keyword = sys.argv[1]

# カレントディレクトリ以下のファイルを対象に処理
for root, dirs, files in os.walk("."):
    for fi in files:
        result = []
        try:
            path = os.path.join(root, fi)
            with open(path, encoding="utf-8") as f:
                for no, line in enumerate(f):
                    if line.find(keyword) >= 0:
                        line = line.strip()
                        s = "| {0:4}: {1}".format(no+1, line)
                        result.append(s)
        except:
            continue

        if len(result) > 0:
            print("+ file: " + fi)
            for li in result:
                print(li)
