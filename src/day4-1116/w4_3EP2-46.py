# -*- coding: utf-8 -*-
# 2017/11/16(木)
# Author : Ryoga Miyamoto
from __future__ import print_function

def prime_generator():
    """素数のジェネレータ"""
    num = 2
    while True:
        # 2～num - 1まででnumを割り切れる数があるか
        if not [i for i in range(2, num) if num % i == 0]:
            yield num
        num += 1

def fibonacci_generator():
    """フィボナッチ数列のジェネレータ"""
    old, new = 0, 1
    while True:
        yield old
        old, new = new, old + new

pn = prime_generator()
fn = fibonacci_generator()

prime = list()
fibonacci = list()
limit = 20              # 繰り返し回数
cnt = 0                 # ループカウンタ
while cnt < limit:
    prime.append(next(pn))
    fibonacci.append(next(fn))
    cnt += 1

print("呼び出し回数 :", limit)
print("素数リスト       :", prime)
print("フィボナッチ数列 :", fibonacci)
