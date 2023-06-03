#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        btn1 = QPushButton()
        btn2 = QPushButton()
        btn3 = QPushButton()
        btn1.setText(str(1))
        btn2.setText(str(2))
        btn3.setText(str(3))

        # addSpacing (1) означает установить масштабирование равным 1
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addStretch(1)
        hbox.addWidget(btn2)
        hbox.addStretch(9)
        hbox.addWidget(btn3)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle('addStretch')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())