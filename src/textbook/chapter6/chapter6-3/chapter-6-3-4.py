# -*- coding: utf-8 -*-
# staticmethod

class Hoge:
    @staticmethod
    def introduce():
        print("Hoge")

# インスタンス化せずに直接メソッドにアクセス
Hoge.introduce()

