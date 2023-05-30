import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    hist_text = ''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400, 400)


        self.labelHist = QLabel(self)
        self.labelHist.resize(400, 200)
        self.labelHist.setText('')
        self.labelHist.setAlignment(Qt.AlignBottom|Qt.AlignLeft)


        self.txtEdit = QTextEdit(self)
        self.txtEdit.move(0, 300)
        self.txtEdit.resize(360, 80)

        self.btnSend = QPushButton(self)
        self.btnSend.move(360, 300)
        self.btnSend.resize(40, 40)
        self.btnSend.clicked.connect(self.btnSend_clicked)

        self.btnAdditions = QPushButton(self)
        self.btnAdditions.move(360, 340)
        self.btnAdditions.resize(40, 40)

    def btnSend_clicked(self):
        self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()
        self.labelHist.setText(self.hist_text)
        self.txtEdit.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













