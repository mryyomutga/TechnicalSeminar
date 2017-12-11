# -*- coding: utf-8 -*-
import json, urllib.request

class Kawase:
    API = "http://api.aoikujira.com/kawase/json/usd"
    def __get_api(self):
        res = urllib.request.urlopen(Kawase.API)
        return res.read().decode("utf8")

    def __analize_result(self, json_str):
        return json.loads(json_str)

    def get_result(self):
        json_str = self.__get_api()
        return self.__analize_result(json_str)

    @staticmethod
    def get_usd_jpy():
        kawase = Kawase()
        data = kawase.get_result()
        usd = data.get("JPY", -1)
        return usd

print("USD:JPY = 1:", Kawase.get_usd_jpy())

