# -*- coding; utf-8 -*-
# 抽象基底クラス

from abc import ABCMeta, abstractmethod

class MazeRobot(metaclass = ABCMeta):
    @abstractmethod
    def init_robot(self):
        pass

    @abstractmethod
    def choose_dir(self):
        pass

class MazeRobotTest(MazeRobot):
    def init_robot(self):
        print("ロボットの初期化")

    def choose_dir(self):
        print("go straight")

robot = MazeRobotTest()
robot.init_robot()
robot.choose_dir()
