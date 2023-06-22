import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *

class Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.msg_as_txt = ""
        self.vbox_tab_layout = QVBoxLayout(self)
        self.splitter = QSplitter(Qt.Vertical)
        self.txt_browser = QTextBrowser(self)
        self.txt_edit = QTextEdit(self)
        self.txt_edit.textChanged.connect(self.txt_edit_changed)


        self.splitter.addWidget(self.txt_browser)
        self.splitter.addWidget(self.txt_edit)
        # self.splitter.setContentsMargins(0, 0, 0, 0)
        self.vbox_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.vbox_tab_layout.addWidget(self.splitter)

        # self.txtBrowser.resize(100, 80)
        # self.txt_Browser.setText('')
        # self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # self.txtEdit.move(0, 300)
        # self.txtEdit.resize(100, 50)
        # self.txt_Edit.textChanged.connect(self.txtEdit_changed)

        self.splitter.setChildrenCollapsible(False)
        self.splitter.setSizes([300, ])

    def txt_edit_changed(self):
        self.msg_as_txt = self.txt_edit.toPlainText()
        cursor = self.txt_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.txt_edit.setTextCursor(cursor)
