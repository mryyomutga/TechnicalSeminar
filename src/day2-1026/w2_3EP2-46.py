# -*- coding: utf-8 -*-
# 2017/10/26(木) 専門ゼミ 第2回 課題
# Author : Ryoga Miyamoto

# 所持金以内で選択したものを購入できるかを判定するプログラム
# 購入できる場合、その内訳と合計金額を表示する

# 買い物かごに商品を入れる関数
def put_in():
    global act, basket, payment
    payment += catalog[act[0]] * int(act[1]) * tax

    # 買い物かごの中に選んだ商品がない場合
    if act[0] not in basket:
        # basketに商品と個数を紐づけて格納
        basket.update({act[0]:int(act[1])})
    else:
        # 個数を加える
        basket[act[0]] += int(act[1])

# 辞書の要素の一覧を表示する関数
def look_in(dic, title="[買い物かご]", unit="個"):
    print("{0:^15}".format(title))
    print("--------------------")
    for key, value in dic.items():
        print("{0:<10}: {1:>4} {2}".format(key, value, unit))
    print("--------------------")

# 所持金
myCash = 5000
# 支払金額
payment = 0
# 消費税
tax = 1.08
# 買い物かごの生成(商品:個数)
basket = dict()
# basket ={}
# 商品カタログの生成
catalog = dict()

# A店の商品一覧
store1 = {"りんご":80, "バナナ":100, "みかん":50,
          "牛肉":900, "豚肉":600, "鶏肉":500,
          "牛乳":100, "パン":120, "たまご":200}

# B店の商品一覧(A店の英語版 入力の簡略化)
store2 = {"apple":80, "banana":100, "orange":50,
          "beef":900, "pork":600, "chicken":500,
          "milk":100, "bread":120, "egg":200}

# catalogをアップデート
catalog.update(store2)

look_in(catalog, "[商品一覧]", "円")

print("------------------------------------------------------------------------")
print("あなたの所持金は{0}円です。".format(myCash))
print("ほしい商品と個数を \"商品,個数\" で指定してください")
print("\"check\" と入力すると、買い物かごの中にある商品、個数、合計金額が見れます")
print("\"pay\" と入力すると精算を行います")
print("------------------------------------------------------------------------")

while True:
    # ユーザーからの入力
    # actを(コンマ区切りで)リスト化
    act = input("商品,個数 : ").split(",")

    # 店にある商品を選択した場合
    if act[0] in catalog and act[1] != "":
        put_in()

    # check
    elif act[0] == "check":
        look_in(basket)
        print("支払金額  : {0:>4} 円".format(int(payment)))
    # pay
    elif act[0] == "pay":
        break
    # 不正な入力
    else:
        print("選択した商品はありません")

    print()

print("精算します\n")
payment = int(payment)
# 所持金以内の場合
if payment <= myCash:
    myCash -= payment
    look_in(basket, "購入リスト")
    print("支払金額  : {0:>4} 円".format(payment))
    print("所持金    : {0:>4} 円".format(myCash))
# 所持金オーバー
else:
    look_in(basket, "購入リスト")
    print("支払金額   : {0:>4} 円".format(payment))
    print("{0}円不足しているので買えませんでした".format(payment - myCash))

print()
