# -*- coding: utf-8 -*-
# デスクトップアプリケーションの作成2
# ファイル選択ダイアログ
import tkinter.filedialog as fd

path = fd.askopenfilename(
    title="ファイルを選択してください",
    filetypes=[("python", "py")]
)
print(path)
