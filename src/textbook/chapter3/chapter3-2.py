# -*- coding: utf-8 -*-
# 辞書型
fruits = {"apple":100, "banana":120, "orange":80}
print(fruits)
print(fruits["apple"])

# 値の更新
fruits["apple"] = 75
print(fruits)

# キーの確認
print("apple" in fruits)
print("lemon" in fruits)

# キーの取得
for i in fruits.keys():
    print(i)
# 値の取得
for v in fruits.values():
    print(v)
# キーと値の取得
for i, v in fruits.items():
    print(i, v)
