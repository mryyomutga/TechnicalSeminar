# -*- coding: utf-8 -*-
# 学習させる
from sklearn import datasets, cross_validation, svm, metrics

# 手書き数字データの読み込み
digits = datasets.load_digits()

# データ分割
data_train, data_test, label_train, label_test = \
    cross_validation.train_test_split(digits.data, digits.target)

# SVMアルゴリズムでモデル構築
clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

# テストデータでの分類結果予測
predict = clf.predict(data_test)

# 結果の表示
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("分類器の情報 =", clf)
print("正解率 =", ac_score)
print("レポート =\n", cl_report)
