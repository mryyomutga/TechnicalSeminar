# -*- coding: utf-8 -*-
# リスト内包表記
data = [i * 2 for i in range(1, 6)]
print(data)

data = list(map(lambda x: x * 2, range(1, 6)))
print(data)

# 奇数のリスト
data = [i * 2 - 1 for i in range(1, 6)]
print(data)
data = [i for i in range(1, 11, 2)]
print(data)
data = [i for i in range(1, 11) if i % 2 == 1]
print(data)

# ネストした内包表記
result = []
base = [1, 2, 3]
for x in base:
    for y in base:
        result.append((x, y))
print(result)

result = [(x, y) for x in base for y in base]
print(result)

result = [(x, y) for x in base for y in base if x != y]
print(result)

# 三項演算子とリスト内包表記
res = ["Fizz Buzz" if i % 15 == 0 else "Fizz"
                   if i % 3 == 0 else "Buzz"
                   if i % 5 == 0 else str(i)
       for i in range(1, 21)
       ]

print("\n".join(res))

# セット内包表記
data = {(x + y) for x in [1, 2, 3] for y in [1, 2, 3]}
print(data)

data = {"h"+str(x):x * 5 for x in range(1, 4)}
print(data)

# ジェネレータを生成
gen = (x ** 2 for x in [1, 2, 3])
for i in gen:
    print(i)
