# -*- coding: utf-8 -*-
# 制御構文 if - elif - else

temp = float(input("今日の気温は? : "))

if temp >= 25:
    print("氷水を出す")
# python3ではandを付けなくても 15 <= temp < 25とかける
elif temp < 25 and temp >= 15:
    print("水を出す")
else:
    print("温めたお茶を出す")

num = 5
if num == 3:
    # 何もしない場合passを記述
    pass
else:
    print(num)
