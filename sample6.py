#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QFormLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вложенный макет')

        self.resize(700, 200)

        # Глобальный элемент управления (обратите внимание на параметр self), используемый для переноса глобального макета
        wwg = QWidget(self)

        # Глобальный макет
        wl = QHBoxLayout(wwg)
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        flayout = QFormLayout()

        # Добавить элементы управления для локального макета
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        glayout.addWidget(QPushButton(str(5)), 0, 0)
        glayout.addWidget(QPushButton(str(6)), 0, 1)
        glayout.addWidget(QPushButton(str(7)), 1, 0)
        glayout.addWidget(QPushButton(str(8)), 1, 1)
        flayout.addWidget(QPushButton(str(9)))
        flayout.addWidget(QPushButton(str(10)))
        flayout.addWidget(QPushButton(str(11)))
        flayout.addWidget(QPushButton(str(12)))

        # Добавить локальный макет в макет wl
        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(flayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())