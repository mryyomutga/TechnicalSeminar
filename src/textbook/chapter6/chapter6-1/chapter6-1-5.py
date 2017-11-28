# -*- coding: utf-8 -*-
# オブジェクト指向について5
# クラス変数とインスタンス変数
class Cat:
    """猫クラス"""
    # クラス変数
    nakigoe = "nya"

    def naku(self):
        # Catクラスのクラス変数にアクセス
        # クラス名.クラス変数名
        print(Cat.nakigoe)

    def naku2(self):
        # インスタンス変数を返す
        print(self.nakigoe)

nora = Cat()
nora.naku()

mike = Cat()
# インスタンス.クラス変数でクラス変数にアクセス
print(nora.nakigoe)

Cat.nakigoe = "myu"

nora.naku()
print(nora.nakigoe)

# nakigoeというインスタンス変数を生成
mike.nakigoe = "nya"

nora.naku2()
mike.naku2()
