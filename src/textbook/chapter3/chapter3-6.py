# -*- coding: utf-8 -*-
# イテレータ
# 値を1つずつ順に取り出す仕組みを持つオブジェクト
num = [1, 2, 3]
# リストからイテレータを生成
i = iter(num)
# イテレータから値を取り出す
# 全て取り出すとStopIteration
print(next(i))
print(next(i))
print(next(i))
# rangeからイテレータを生成
i = iter(range(1, 4))
print(next(i))
print(next(i))
print(next(i))

# ジェネレータ(自作のイテレータを作成する)
def gen1to3():
    yield 1
    yield 2
    yield 3
it = gen1to3()
for i in it:
    print(i)

i = gen1to3()
print(next(i))
print(next(i))
print(next(i))

# 奇数を返すイテレータ
def genOdd(maxnum):
    i = 1
    while i <= maxnum:
        yield i
        i += 2
it = genOdd(50)
for i in it:
    print(i, end=",")
print()

# 素数を返すイテレータ
def genPrime(maxnum):
    num = 2
    while num <= maxnum:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1
it = genPrime(50)
for i in it:
    print(i, end=",")
