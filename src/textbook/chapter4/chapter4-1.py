# -*- coding: utf-8 -*-
# モジュール
import calculater as calc
a = 10
b = 4
print(calc.add(a, b))
print(calc.sub(a, b))
print(calc.mul(a, b))
print(calc.div(a, b))

# 関数オブジェクトで利用する
numsum = calc.add
numdif = calc.sub
numpro = calc.mul
numquo = calc.div
print(numsum(10, 4))
print(numdif(10, 4))
print(numpro(10, 4))
print(numquo(10, 4))

# fromで特定のメンバだけ取り出す
from calculater import add
print(add(2, 3))

# 異なるディレクトリのモジュールの利用
# import mod.output
# mod.output.output_val(10)
from mod.output import *
output_val(10)
print()

# 標準ライブラリ
# randomモジュール
import random
r = random.randint(1, 6)
print(r)

# datetimeモジュール
import datetime
print(datetime.date.today())
t = datetime.datetime.now()
print(t.strftime("%Y/%m/%d %H:%M:%S"))
