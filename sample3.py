#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton(str(1)), 0, Qt.AlignTop)
        hbox.addWidget(QPushButton(str(2)), 0, Qt.AlignTop | Qt.AlignLeft)
        hbox.addWidget(QPushButton(str(3)), 0)
        hbox.addWidget(QPushButton(str(4)), 0, Qt.AlignLeft | Qt.AlignBottom)
        hbox.addWidget(QPushButton(str(5)), 0, Qt.AlignTop)

        self.setLayout(hbox)
        self.setWindowTitle('Горизонтальный макет')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())