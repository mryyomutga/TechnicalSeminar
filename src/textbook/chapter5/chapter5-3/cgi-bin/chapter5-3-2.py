# -*- coding: utf-8 -*-
# 1行チャット
import cgi
import cgitb
import os.path
import html

# デバッグモードの有効化
cgitb.enable()

# 全体の設定
FILE_LOG = "chat_log.txt"

# HTMLを画面に出力
def print_html(body):
    # ヘッダ情報の出力
    print("Content-Type: text/html; charset=shift_jis\n")
    print("""
          <html><head><meta charset="shift_jis" />
          <title>1行チャット</title></head><body>
          <h1>チャット</h1>
          <div><form>
          名前 : <input type="text" name="name" size="8" />
          本文 : <input type="text" name="body" size="20" />
          <input type="submit" value="発言" />
          <input type="hidden" name="mode" value="write" />
          </form></div><hr>
          {0}
          </body></html>
          """.format(body)
          )

# チャットログの表示
def mode_read(form):
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding="utf-8") as f:
            log = f.read()
    print_html(log)

# リンクへのジャンプ
def jump(url):
    print("Status: 301 Moved Permanently")
    print("Location: " + url)
    print()

    print("<html><head>")
    print("<meta http-equiv='refresh' content='0;" + url + "'>")
    print("</head><body>")
    print("<a href='" + url + "'>jump</a></body></html>")

# メッセージの書き込み
def mode_write(form):
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")

    # HTML変換
    name = html.escape(name)
    body = html.escape(body)
    # ファイルに保存
    with open(FILE_LOG, "a+", encoding="utf-8") as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name, body))
    # リダイレクト
    jump("chapter5-3-2.py")

def main():
    # フォームデータの取得
    form = cgi.FieldStorage()
    # modeパラメータの取得
    mode = form.getvalue("mode", "read")

    if mode == "read":
        mode_read(form)
    elif mode == "write":
        mode_write(form)
    else:
        mode_read(form)

if __name__ == "__main__":
    main()
