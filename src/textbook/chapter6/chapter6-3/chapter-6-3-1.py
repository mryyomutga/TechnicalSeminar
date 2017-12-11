# -*- coding: utf-8 -*-
# 非公開メンバと静的メソッド

class Game:
    def __goal(self):
        print("非公開メソッド")

    def play(self):
        print("公開メソッド")

game = Game()
game.play()

# 非公開メソッドにアクセスできない
game.__goal()


