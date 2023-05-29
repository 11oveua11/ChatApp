import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400,400)


        self.labelHist = QLabel(self)
        self.labelHist.resize(400,200)


        self.ledText = QLineEdit(self)
        self.ledText.move(0,300)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())