# -*- coding: utf-8 -*-
# オブジェクト指向について1
# クラス内で定義した関数 : メソッド
# クラス内で定義した変数 : プロパティ
class Human:
    """人間クラス"""
    def setName(self, name):
        """名前の設定"""
        self.name = name

    def getName(self):
        """自分の名前を取得する"""
        return self.name

    def search(self, place):
        """周りを見る"""
        pass

    def take(self, food):
        """物をつかむ"""
        self.food = food

    def open_mouth(self):
        """口を開ける"""
        pass

    def eat(self):
        """食べる"""
        print(self.food + "を食べました")

# クラスをもとにインスタンスを生成
hito = Human()
hito.take("食パン")
hito.eat()

hito.setName("Bob")
print(hito.getName())   # getNameメソッドの呼び出し
print(hito.name)        # nameプロパティの取得
