# -*- coding: utf-8 -*-
# デスクトップアプリケーションの作成3
# ボタンとウィンドウ
from tkinter import *
import tkinter.messagebox as mb

def say_hello():
    """ボタンが押されたときのイベント"""
    mb.showinfo("挨拶", "Hello!!")

# メインウィンドウの生成
root = Tk()
root.title("挨拶")

# ラベル生成
desc_label = Label(text = "以下のボタンを押してください")
desc_label.pack()

# ボタン生成
hello_button = Button(
    text = "挨拶",
    width = 8, height = 3,
    command = say_hello
)

hello_button.pack()

root.mainloop()
