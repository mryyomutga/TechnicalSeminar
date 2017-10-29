# -*- coding: utf-8 -*-
# 制御構文 while, for

# while
# 無限ループ
while True:
    user = input("坪数 : ")
    # 終了条件
    if user == "" or user == "q":
        break
    tubo = int(user)
    m2 = tubo * 3.31
    print("{0}坪は {1}平方メートル".format(tubo, m2))

# for
v = 0
for i in range(1, 11):
    v += i
    print(i, "を足すと", v)
print("1から10までの総和は", v)

# continue
for i in range(5):
    print("i =", i)
    if i % 2 == 0:
        continue
    print("-- Hello")
# else
num = 8
while num < 5:
    print("while(in)=", num)
    num += 1
else:
    print("while(else)=", num)

i = 3
while i < 5:
    print("while(in)=", i)
    if i == 2:
        break
    i += 1
# breakでループを抜けなかった時
else:
    print("while(else)=", i)
