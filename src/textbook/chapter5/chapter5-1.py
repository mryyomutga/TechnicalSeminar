# -*- coding: utf-8 -*-
# デスクトップアプリケーションの作成
import tkinter.messagebox as mb
# ダイアログの表示
ans = mb.askyesno("質問", "数学は好きですか?")
if ans == True:
    mb.showinfo("同意","僕も好きです")
else:
    mb.showinfo("本当?", "まさか、数学が嫌いだなんて")
