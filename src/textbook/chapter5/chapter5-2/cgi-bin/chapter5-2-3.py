# -*- coding: utf-8 -*-
# Webアプリケーションの作成3
# URLパラメータの取得
import cgi
import cgitb

# デバッグモードの有効化
cgitb.enable()

# ヘッダ情報の出力
print("Content-Type: text/html; charset=shift-jis\n")

print("<pre>")
# URLパラメータの取得
form = cgi.FieldStorage()

# 特定のパラメータを取得
mode = form.getvalue("mode", default="")
print("mode =", mode)

# 全てのパラメータを取得
print("--- all params ---")

for k in form.keys():
    print(k, "=", form.getvalue(k))
