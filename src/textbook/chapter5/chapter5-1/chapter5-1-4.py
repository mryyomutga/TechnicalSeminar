# -*- coding: utf-8 -*-
# デスクトップアプリケーションの作成4
# テキストカウンタ
from tkinter import *

def count_text(event):
    """テキストの文字数をカウント"""
    s = main_text.get(1.0, END)
    info_label.config(text = "{0}文字".format(len(s)))

# メインウィンドウの生成
root = Tk()
root.title("テキストカウンタ")

# テキストボックスの生成
main_text = Text(root)
main_text.bind("<Key>", count_text)
main_text.pack()

# 文字数表示のラベルの生成
info_label = Label(root)
info_label.pack()

root.mainloop()
