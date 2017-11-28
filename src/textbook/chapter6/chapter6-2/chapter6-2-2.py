# -*- coding: utf-8 -*-
# メソッドのオーバーライド
class SuperClass:
    def hoge(self):
        print("Superclass.hoge")

class SubClass(SuperClass):
    # スーパークラスと同名のメソッドを定義
    def hoge(self):
        print("SubClass.hoge")
it1 = SuperClass()
it2 = SubClass()
it1.hoge()
it2.hoge()
