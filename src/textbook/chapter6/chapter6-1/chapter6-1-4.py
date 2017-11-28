# -*- coding: utf-8 -*-
# オブジェクト指向について4
# 複数のクラスを扱う
class Student:
    """生徒クラス"""

    def __init__(self, id, name, score = 0):
        """コンストラクタ"""
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        """IDを取得する"""
        return self.id

    def getName(self):
        """生徒名を取得する"""
        return self.name

    def setScore(self, score):
        """点数を設定する"""
        self.score = score

    def getScore(self):
        """点数を取得する"""
        return self.score

class CalcScore:
    """点数計算クラス"""

    def __init__(self):
        """コンストラクタ"""
        self.students = list()

    def addStudent(self, student):
        """学生を追加する"""
        self.students.append(student)

    def average(self):
        v = 0

        for i in self.students:
            v += i.getScore()
        ave_v = v / len(self.students)
        return ave_v

# インスタンスを生成
p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score = 79)
p3 = Student(12, "佐々木", score = 84)
p4 = Student(13, "井上", score = 77)

calc = CalcScore()
calc.addStudent(p1)
calc.addStudent(p2)
calc.addStudent(p3)
calc.addStudent(p4)
print("平均点 =", calc.average())
