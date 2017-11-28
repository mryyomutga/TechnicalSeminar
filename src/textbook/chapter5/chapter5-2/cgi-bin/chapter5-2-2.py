# -*- coding: utf-8 -*-
# Webアプリケーションの作成2
# サイコロの実装
import random
# ヘッダ情報の出力
print("Content-Type: text/html\n")

num = random.randint(1, 6)
body = """
<html>
<head><title>Dice Roll</title></head>
<body>
    <h1>Dice : {num}</h1>
</body>
</html>
""".format(num = num)

print(body)
