import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *


class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400, 400)
        self.setWindowIcon(QIcon('icon1.png'))

        # self.message = AdvMessage()
        self.msg_as_txt_0 = ""

        self.txt_Browser_0 = QTextBrowser(self)
        #self.txtBrowser.resize(100, 80)
        self.txt_Browser_0.setText('')
        # self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.txt_Edit_0 = QTextEdit(self)
        # self.txtEdit.move(0, 300)
        #self.txtEdit.resize(100, 50)
        self.txt_Edit_0.textChanged.connect(self.txtEdit_changed)

        self.tabWidget = QTabWidget(self)
        self.tab_0 = QWidget()
        self.vbox_tab_layout_0 = QVBoxLayout(self.tab_0)
        # self.tab_0.setStyleSheet('background-color: red')
        self.splitter_0 = QSplitter(Qt.Vertical)
        self.splitter_0.addWidget(self.txt_Browser_0)
        self.splitter_0.addWidget(self.txt_Edit_0)
        self.splitter_0.setChildrenCollapsible(False)
        self.splitter_0.setSizes([300, ])
        self.vbox_tab_layout_0.addWidget(self.splitter_0)
        # self.tab_0.resize(self, [350, 300])

        # self.splitter_0.setSizes([240, 100])


        self.vbox_main_layout = QVBoxLayout(self)
        self.vbox_main_layout.addWidget(self.tabWidget)
        self.tabWidget.addTab(self.tab_0, "Tab 0")



        self.hbox_layout = QHBoxLayout(self)

        self.btnSend = QPushButton(self)
        # self.btnSend.move(360, 300)
        # self.btnSend.resize(40, 40)
        self.btnSend.clicked.connect(self.btnSend_clicked)
        self.btnSend.setIcon(QIcon('send-icon.png'))

        self.btnAdditions = QPushButton(self)
        # self.btnAdditions.move(360, 340)
        # self.btnAdditions.resize(40, 40)
        self.btnAdditions.clicked.connect(self.btnAdditions_clicked)
        self.btnAdditions.setIcon(QIcon('emoji-icon.png'))

        self.btnTemp = QPushButton(self)
        self.btnTemp.clicked.connect(self.add_new_tab)

        self.hbox_layout.addWidget(self.btnSend)
        self.hbox_layout.addWidget(self.btnAdditions)
        self.hbox_layout.addWidget(self.btnTemp)

        self.vbox_main_layout.addLayout(self.hbox_layout)



    def add_new_tab(self):

        self.msg_as_txt_0 = ""

        self.txt_Browser_0 = QTextBrowser(self)
        # self.txtBrowser.resize(400, 300)
        self.txt_Browser_0.setText('')
        self.txt_Browser_0.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.txt_Edit_0 = QTextEdit(self)
        # self.txtEdit.move(0, 300)
        # self.txtEdit.resize(400, 80)
        self.txt_Edit_0.textChanged.connect(self.txtEdit_changed)

        self.splitter_0 = QSplitter(Qt.Vertical)
        self.splitter_0.addWidget(self.txt_Browser_0)
        self.splitter_0.addWidget(self.txt_Edit_0)

        self.vbox_main_layout = QVBoxLayout(self)
        self.vbox_main_layout.addWidget(self.splitter_0)

    def btnSend_clicked(self):
        # self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()

        self.txt_Browser_0.append(emoji.emojize(self.msg_as_txt_0))
        self.txt_Edit_0.clear()
        self.txt_Edit_0.setFocus()

    def btnAdditions_clicked(self):
        self.msg_as_txt_0 = self.txt_Edit_0.toPlainText() + ':thumbs_up:'
        self.txt_Edit_0.setText(emoji.emojize(self.msg_as_txt_0))
        self.txt_Edit_0.setFocus()



    def send_message (self, msg_param):
        pass

    def txtEdit_changed(self):
        self.msg_as_txt_0 = self.txt_Edit_0.toPlainText()
        cursor = self.txt_Edit_0.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.txt_Edit_0.setTextCursor(cursor)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













