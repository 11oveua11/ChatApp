import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *

class Tabs(QWidget):
    def __init__(self):
        super().__init__()
        self.msg_as_txt = ""
        self.vbox_tab_layout = QVBoxLayout(self)
        self.splitter = QSplitter(Qt.Vertical)
        self.txt_Browser = QTextBrowser(self)
        self.txt_Edit = QTextEdit(self)

        self.splitter.addWidget(self.txt_Browser)
        self.splitter.addWidget(self.txt_Edit)
        self.vbox_tab_layout.addWidget(self.splitter)

        # self.txtBrowser.resize(100, 80)
        # self.txt_Browser.setText('')
        # self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # self.txtEdit.move(0, 300)
        # self.txtEdit.resize(100, 50)
        # self.txt_Edit.textChanged.connect(self.txtEdit_changed)

        self.splitter.setChildrenCollapsible(False)
        self.splitter.setSizes([300, ])
        self.vbox_tab_layout.setContentsMargins(0, 0, 0, 0)