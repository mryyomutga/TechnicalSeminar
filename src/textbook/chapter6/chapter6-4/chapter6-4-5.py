# -*- coding : utf-8 -*-
# 特殊メソッド5
# アクセサ

class Clock:
    def __init__(self, hour):
        self._hour = hour
        self._ampm = "am"

    @property
    def hour(self):
        return self._hour

    @property
    def ampm(self):
        return self._ampm

    # @ゲッター名.setter
    @hour.setter
    def hour(self, value):
        self._hour = value % 12
        self._ampm = "am" if value <= 12 else "pm"

obj = Clock(11)
print(obj.hour, obj.ampm)
obj.hour = 13
print(obj.hour, obj.ampm)
