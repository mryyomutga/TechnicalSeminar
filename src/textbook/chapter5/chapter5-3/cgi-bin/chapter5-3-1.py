# -*- coding: utf-8 -*-
# Webアプリケーションの作成4
# 足し算プログラム
import cgi

# ヘッダ情報の出力
print("Content-Type: text/html; charset=shift_jis\n")

# フォームデータの取得
form = cgi.FieldStorage()

# フォームデータの確認
if not "v1" in form or not "v2" in form:
    fs = """
    <form>
    <input type="text" name="v1" /> +
    <input type="text" name="v2" />
    <input type="submit" value="計算" />
    </form>
    """
    print(fs)
else:
    v1 = form.getvalue("v1", "0")
    v2 = form.getvalue("v2", "0")
    try:
        ans = int(v1) + int(v2)
    except:
        ans = 0
    print("<h1>", ans, "</h1>")
