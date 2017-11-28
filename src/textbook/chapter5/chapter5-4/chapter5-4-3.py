# -*- coding: utf-8 -*-
# 手書き数字の画像を認識させる
import os, sys, math
from sklearn import datasets, svm
from sklearn.externals import joblib

# モデルデータファイル
DIGITS_PKL = "digit-clf.pkl"

# 予測モデルの作成
def train_digits():
    # 手書き数字データの読み込み
    digits = datasets.load_digits()

    # training
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma=0.001)
    clf.fit(data_train, label_train)

    # 予測モデルの保存
    joblib.dump(clf, DIGITS_PKL)
    print("予測モデルを保存しました =", DIGITS_PKL)
    return clf

# データから数字を予測
def predict_digits(data):
    # モデルファイルの読み込み
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)

    # 予測開始
    n = clf.predict([data])
    print("判定結果 =", n)

# 手書き数字画像の変換
def image_to_data(imagefile):
    import numpy as np
    from PIL import Image
    image = Image.open(imagefile).convert("L")
    image = image.resize((8, 8), Image.ANTIALIAS)
    img = np.asarray(image, dtype=float)
    img = np.floor(16 - 16 * (img / 256))

    # 画像表示
    import matplotlib.pyplot as plt
    plt.imshow(img)
    plt.gray()
    plt.show()

    img = img.flatten()
    print(img)
    return img

def main():
    if len(sys.argv) <= 1:
        print("USAGE:")
        print("python chapter5-4-3.py imagefile")
        return
    imagefile = sys.argv[1]
    data = image_to_data(imagefile)
    predict_digits(data)

if __name__ == "__main__":
    main()
