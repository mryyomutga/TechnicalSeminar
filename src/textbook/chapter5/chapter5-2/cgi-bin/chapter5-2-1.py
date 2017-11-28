# -*- coding: utf-8 -*-
# Webアプリケーションの作成1
# サーバ起動コマンド
# python -m http.server --cgi port
# 文字化けする場合(windows)
# 1. htmlの文字コードをshift-jisにする
# 2. 最初は英数字から始める
# ヘッダ情報の出力
print("Content-type: text/html; charset=shift-jis")
print()
# html
print("<html><head><meta charset='shift-jis'><body>")
print("聞くことに速く語ることに遅くあるべき")
print("</body></html>")
