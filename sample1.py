#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lb1 = QLabel('Добро пожаловать', self)
        lb1.move(15, 10)
        lb2 = QLabel('Учиться', self)
        lb2.move(35, 40)
        lb3 = QLabel('PyQt 5', self)
        lb3.move(55, 70)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt  Абсолютное позиционирование в 5 ')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())