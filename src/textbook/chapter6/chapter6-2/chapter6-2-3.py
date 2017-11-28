# -*- coding: utf-8 -*-
# メソッドのオーバーライド
class SuperClass:
    def hoge(self, id):
        print("---")
        print("SuperClass.hoge =", id)

class SubClass(SuperClass):
    def hoge(self, id):
        super().hoge(id)
        print("SubClass.hoge =", id)

rc = SuperClass()
rc.hoge(100)

sc = SubClass()
sc.hoge(300)
