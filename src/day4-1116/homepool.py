from __future__ import print_function
from math import sqrt

print("円が重なっているか判定します")
n = int(input("判定する円の個数: "))
# a, b, R = input("基準となる円の情報(a,b,R): ").split(" ")
# a, b, R = int(a), int(b), int(R)
a, b, R = map(int, input("基準となる円の情報(a,b,R): ").split())
print(type(a), type(b), type(R))
mes = list()
print("調べる円の情報(x,y,r)")
for i in range(n):
    # x, y, r = input().split(" ")
    # x, y, r = int(x), int(y), int(r)
    x, y, r = map(int, input().split())
    d = sqrt(pow(x, 2) + pow(y, 2))
    if d >= R + r:
        mes.append("True")
    else:
        mes.append("False")

for s in mes:
    print(s)
