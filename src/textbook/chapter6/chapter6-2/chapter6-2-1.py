# -*- coding: utf-8 -*-
# クラスの継承
# モジュールを取り込む
import car
# help(car)

car1 = car.Van("Taro")
car1.turn_left()
car1.show_status()

car2 = car.Camper("Jiro")
car2.turn_right()
car2.show_status()
car2.make_ice()
