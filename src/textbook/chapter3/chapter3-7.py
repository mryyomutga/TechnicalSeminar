# -*- coding: utf-8 -*-
# 例外処理
def judge_bmi():
    result = ""
    while True:
        try:
            weight = float(input("kg? "))
            height = float(input("cm? "))
            height = height / 100
            bmi = weight / (height * height)
            break
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except:
            print("その他のエラー")
        # 必ず最後に実行する
        # finally:
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi < 25:
        result = "標準体型"
    elif bmi < 30:
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
    return result

print(judge_bmi())

# エラーの発生
# raise Exception("Sample Error")

def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break
nums = [n for n in range(1, 11)]
for_func(nums, lambda i: print(i))

ages = {"Taro":20, "Jiro":15, "Saburo":10}
for_func(ages.items(), lambda n: print(n))
