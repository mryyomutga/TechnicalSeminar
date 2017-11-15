# -*- coding: utf-8 -*-
# PyPIパッケージの利用
# pycryptoのインストールはREADME.mdに記載
import qrcode
from Crypto.Cipher import AES
import base64

# QRコードの生成
img = qrcode.make("https://github.com/mryyomutga")
img.save("myAccount.png")

# pycryptoで暗号化と復号化
message = "I like math, but I don't like Japanese."
password = "mryyomutga"
iv = "L14fg6dWb7jsOopy"     # 初期化ベクトル
mode = AES.MODE_CBC         # 暗号化モードの指定

def mkpad(s, size):
    s = s.encode("utf-8")
    pad = b' ' * (size - len(s) % size)
    return s + pad

def encrypt(password, data):
    password = mkpad(password, 16)
    data = mkpad(data, 16)
    password = password[:16]

    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")

def decrypt(password, encdata):
    password = mkpad(password, 16)
    password = password[:16]

    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")

enc = encrypt(password, message)
dec = decrypt(password, enc)

print("暗号化 :", enc)
print("復号化 :", dec)
