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

        self.message = AdvMessage()
        self.msg_as_txt = ""

        # self.frame_bottom = QFrame(self)
        # self.frame_bottom.setFrameShape(QFrame.StyledPanel)

        self.txtBrowser = QTextBrowser(self)
        self.txtBrowser.resize(400, 300)
        self.txtBrowser.setText('')
        self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.txtEdit = QTextEdit(self)
        # self.txtEdit.move(0, 300)
        self.txtEdit.resize(400, 80)
        self.txtEdit.textChanged.connect(self.txtEdit_changed)

        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.txtBrowser)
        self.splitter.addWidget(self.txtEdit)

        self.vbox_main_layout = QVBoxLayout(self)
        self.vbox_main_layout.addWidget(self.splitter)

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

        self.hbox_layout.addWidget(self.btnSend)
        self.hbox_layout.addWidget(self.btnAdditions)


        self.vbox_main_layout.addLayout(self.hbox_layout)


    def btnSend_clicked(self):
        # self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()

        self.txtBrowser.append(emoji.emojize(self.msg_as_txt))
        self.txtEdit.clear()
        self.txtEdit.setFocus()

    def btnAdditions_clicked(self):
        self.msg_as_txt = self.txtEdit.toPlainText() + ':thumbs_up:'
        self.txtEdit.setText(emoji.emojize(self.msg_as_txt))
        self.txtEdit.setFocus()



    def send_message (self, msg_param):
        pass

    def txtEdit_changed(self):
        self.msg_as_txt = self.txtEdit.toPlainText()
        cursor = self.txtEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.txtEdit.setTextCursor(cursor)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













