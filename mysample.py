import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSplitter, QTextEdit, \
    QApplication, QFrame
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *


class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400, 400)
        self.setWindowIcon(QIcon('icon2.png'))

        self.vbox_main = QVBoxLayout()
        self.splitter = QSplitter(Qt.Vertical)
        self.hbox_bottom = QHBoxLayout()


        self.message = AdvMessage()
        self.msg_as_txt = ""

        self.txtBrowser = QTextBrowser(self)
        self.txtBrowser.resize(400, 300)
        self.txtBrowser.setText('')
        # self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        self.txtEdit = QTextEdit(self)
        self.txtEdit.move(0, 300)
        self.txtEdit.resize(360, 80)
        self.txtEdit.textChanged.connect(self.txtEdit_changed)

        self.btnSend = QPushButton(self)
        self.btnSend.move(360, 300)
        self.btnSend.resize(40, 40)
        self.btnSend.clicked.connect(self.btnSend_clicked)
        self.btnSend.setIcon(QIcon('Icon5.png'))

        self.btnAdditions = QPushButton(self)
        self.btnAdditions.move(360, 340)
        self.btnAdditions.resize(40, 40)
        self.btnAdditions.clicked.connect(self.btnAdditions_clicked)
        self.btnAdditions.setIcon(QIcon('emoji.png'))



        self.splitter.addWidget(self.txtBrowser)
        #self.splitter.addWidget(self.hbox_bottom)
        self.vbox_main.addWidget(self.txtBrowser)
        self.hbox_bottom.addWidget(self.txtEdit)
        self.hbox_bottom.addWidget(self.btnSend)
        self.hbox_bottom.addWidget(self.btnAdditions)

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















    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle('QSplitter')
        self.setGeometry(300, 300, 300, 200)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        txted = QTextEdit(topleft)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        sp1 = QSplitter(Qt.Horizontal)
        te = QTextEdit()
        sp1.addWidget(topleft)
        sp1.addWidget(te)
        sp1.setSizes([100, 200])

        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(bottom)

        hbox.addWidget(sp2)
        self.setLayout(hbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())