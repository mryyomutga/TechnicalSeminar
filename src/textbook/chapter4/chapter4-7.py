# -*- coding: utf-8 -*-
# デコレータ
# デコレータの関数を定義
def show_func_name(func):
    def wrapper(*args, **kwargs):
        print("--- start: " + func.__name__)
        res = func(*args, **kwargs)
        print("--- end: " + func.__name__)
        return res
    return wrapper

# デコレータを使用する
@show_func_name
def kakugen1():
    print("賢い者たちの静かな言葉は、")
    print("愚鈍な人々の叫びよりも聞かれる。")

@show_func_name
def kakugen2():
    print("求め続けなさい。そうすれば与えられます。")

kakugen1()
kakugen2()

# デコレータの関数定義例
# def decorator(func):
#     def wrapper(*args, *kwargs):
#         # 前処理
#         res = func(*args, **kwargs)
#         # 後処理
#         return res
#     return wrapper

# 処理時間計測デコレータ
import time
def time_log(func):
    def wrapper(*args, **kwargs):
        import datetime
        start = datetime.datetime.today()
        print("--- start:", func.__name__)
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        delta = end - start
        print("--- end:", func.__name__, delta, "sec")
    return wrapper
@time_log
def test1():
    print("sleep 2sec")
    time.sleep(2)
@time_log
def test2():
    print("sleep 2sec")
    time.sleep(2)
test1()
test2()

# ネストするデコレータ
def wrap_html(func):
    def wrapper(*args, **kwargs):
        s = "<html>"
        s += func(*args, **kwargs)
        s += "</html>"
        return s
    return wrapper

def wrap_body(func):
    def wrapper(*args, **kwargs):
        s = "<body>"
        s += func(*args, **kwargs)
        s += "</body>"
        return s
    return wrapper
@wrap_html
@wrap_body
def show_html(text):
    return text
print(show_html("ネストするデコレータ"))
