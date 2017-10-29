# -*- coding: utf-8 -*-
# 変数

# 東京-大阪間
dist = 507.5
# 時速
speed = 80

time = dist / speed
print(time)

# inch -> cm
per_inch = 2.54
inch = 8
cm = inch * per_inch
print(cm)

# 値の埋め込み
print("年齢は", 20, "歳です")
print("Hello.", end="")
print("I am 20 years old.")

a, b, h = 2, 3, 4
area = (a + b) * h / 2
print("台形の面積は", area, "cm.", "\n")
