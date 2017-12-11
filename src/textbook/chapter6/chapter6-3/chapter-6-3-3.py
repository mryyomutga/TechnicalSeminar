# -*- coding: utf-8 -*-
# 空のクラス

class Empty:
    pass

calc = Empty()

# 動的にメソッドを追加
calc.x2 = lambda x : x * 2
calc.x3 = lambda x : x * 3

# 追加したメソッドを利用
print(calc.x2(5))
print(calc.x3(5))

