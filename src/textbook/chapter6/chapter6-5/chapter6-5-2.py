# -*- coding: utf-8 -*-
# ダック・タイピング

def test_duck(it):
    it.sound()
    it.walk()

class Duck:
    def sound(self):
        print("ガァガァ")
    def walk(self):
        print("アヒルが歩く")

class Dog:
    def sound(self):
        print("ワンワン")
    def walk(self):
        print("犬が歩く")

class Cat:
    def sound(self):
        print("ニャーニャー")
    def walk(self):
        print("猫が歩く")

# ダック・タイピング
duck = Duck()
test_duck(duck)

dog = Dog()
test_duck(dog)

cat =Cat()
test_duck(cat)
