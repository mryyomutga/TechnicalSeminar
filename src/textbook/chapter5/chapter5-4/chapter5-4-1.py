# -*- coding: utf-8 -*-
# Scikit learnで学習済みデータを利用する
from sklearn import datasets
from matplotlib import pyplot as plt, cm

# 手書き数字データの読み込み
digits = datasets.load_digits()
print(digits.target[0])
print(digits.images[0])
data = digits.images[0]

plt.imshow(data.reshape(8, 8), cmap=cm.gray_r, interpolation="nearest")
plt.show()
