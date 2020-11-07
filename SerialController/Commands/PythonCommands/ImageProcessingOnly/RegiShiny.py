#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand
from Commands.Keys import KeyPress, Button, Direction, Stick
from Utility import sendToSlack
from enum import Enum, auto

class RegiSeries(Enum):
    REGIELEKI = auto()
    REGIDORAGO = auto()



class RegiShiny(ImageProcPythonCommand):
    regi_series = None
    template_file_path = ""

    def __init__(self, cam):
        super().__init__(cam)

    def loop(self):
        counter = 1

        for i in range(4):
            self.press(Button.B, wait=1)

        while True:
            print('厳選回数: %d' % counter)
            if self.regi_series in [RegiSeries.REGIELEKI, RegiSeries.REGIDORAGO] :
                for i in range(4):
                    self.press(Button.A, wait=0.52)
                self.press(Button.A, wait=14.)
            else:
                self.wait(1.)

            if self.is_shiny(counter):
                break

            self.press(Button.HOME, wait=0.45)
            self.press(Button.X, wait=0.38)
            self.press(Button.A, wait=5)
            self.press(Button.A, wait=1.5)
            self.press(Button.A, wait=16.)
            self.press(Button.A, wait=5.)
            counter += 1

    def is_shiny(self, counter):
        # 通常色である場合にFalseを返す
        if self.isContainTemplate(self.template_file_path, threshold=0.7, show_value=True, use_gray=False):
            print("not shiny")
            return False
        return False

class RegielekiShiny(RegiShiny):
    NAME = 'レジエレキ/ドラゴ色厳選'
    regi_series = RegiSeries.REGIELEKI
    template_file_path = 'regieleki_normal.png'
    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        self.loop()
