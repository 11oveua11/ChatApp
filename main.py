import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *
from tabs import *


class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400, 400)
        self.setWindowIcon(QIcon('icon1.png'))

        # self.message = AdvMessage()
        self.msg_as_txt_0 = ""
        self.tab_widget = QTabWidget(self)
        self.cur_tab = 0 # Index of active tab widget
        self.tab_list = []
        # self.msg_as_txt_list = []
        # self.txt_Browser_list = []
        # self.txt_Edit_list = []
        # self.txt_Edit_list_changed = []
        # self.vbox_tab_layout_list = []
        # self.splitter_list = []

        # self.txt_Browser_0 = QTextBrowser(self)
        # self.txtBrowser.resize(100, 80)
        # self.txt_Browser_0.setText('')
        # self.txtBrowser.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

        # self.txt_Edit_0 = QTextEdit(self)
        # self.txtEdit.move(0, 300)
        # self.txtEdit.resize(100, 50)
        # self.txt_Edit_0.textChanged.connect(self.txtEdit_changed)

        self.tab_list.append(Tab())
        self.tab_widget.currentChanged.connect(self.tab_widget_changed)
        self.tab_widget.addTab(self.tab_list[0], "Tab 0")
        #self.tab_0 = QWidget()
        #self.vbox_tab_layout_0 = QVBoxLayout(self.tab_0)
        # self.tab_0.setStyleSheet('background-color: red')
        #self.splitter_0 = QSplitter(Qt.Vertical)
        #self.splitter_0.addWidget(self.txt_Browser_0)
        #self.splitter_0.addWidget(self.txt_Edit_0)
        #self.splitter_0.setChildrenCollapsible(False)
        #self.splitter_0.setSizes([300, ])
        #self.vbox_tab_layout_0.addWidget(self.splitter_0)
        #self.vbox_tab_layout_0.setContentsMargins(0, 0, 0, 0)
        # self.tab_0.resize(self, [350, 300])

        # self.splitter_0.setSizes([240, 100])


        self.vbox_main_layout = QVBoxLayout(self)
        self.vbox_main_layout.setContentsMargins(0, 0, 0, 0)
        self.vbox_main_layout.addWidget(self.tab_widget)
        #self.tab_widget.addTab(self.tab_0, "Tab 0")



        self.hbox_layout = QHBoxLayout(self)
        self.hbox_layout.setContentsMargins(0, 0, 0, 0)

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

        self.tab_list.append(Tab())
        self.tab_widget.addTab(self.tab_list[-1], "Tab " + str(len(self.tab_list) - 1))
        # self.txt_Browser_0.append(str(self.tab_widget.count()))
        # self.txt_Browser_0.append(str(self.tab_widget.currentIndex()))


        # self.tab_ind = len(self.tab_Widget)-1
        # self.msg_as_txt_list.append("")
        #
        # self.tab_list.append(QWidget())
        #
        # self.txt_Browser_list.append(QTextBrowser(self))
        # # self.txtBrowser.resize(400, 300)
        # self.txt_Browser_list[self.tab_ind].setText('')
        # self.txt_Browser_list[self.tab_ind].setAlignment(Qt.AlignBottom | Qt.AlignLeft)
        #
        # self.txt_Edit_list.append(QTextEdit(self))
        # # self.txtEdit.move(0, 300)
        # # self.txtEdit.resize(400, 80)
        # self.txt_Edit_list[self.tab_ind].textChanged.connect(self.txtEdit_changed)
        #
        # self.splitter_list.append(QSplitter(Qt.Vertical))
        # self.splitter_list[self.tab_ind].addWidget(self.txt_Browser_list[self.tab_ind])
        # self.splitter_list[self.tab_ind].addWidget(self.txt_Edit_list[self.tab_ind])
        #
        # self.vbox_tab_layout_list.append(QVBoxLayout(self.tab_list[self.tab_ind]))
        # self.vbox_tab_layout_list[self.tab_ind].addWidget(self.splitter_list[self.tab_ind])
        #
        # self.tab_Widget.addTab(self.tab_list[self.tab_ind], "Chat " + str(self.tab_ind))

    def btnSend_clicked(self):
        pass
        # self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()
        self.tab_list[self.cur_tab].txt_browser.append(emoji.emojize(self.tab_list[self.cur_tab].msg_as_txt))
        self.tab_list[self.cur_tab].txt_edit.clear()
        self.tab_list[self.cur_tab].txt_edit.setFocus()

    def btnAdditions_clicked(self):

        self.tab_list[self.cur_tab].msg_as_txt = self.tab_list[self.cur_tab].txt_edit.toPlainText() + ':thumbs_up:'
        self.tab_list[self.cur_tab].txt_edit.setText(emoji.emojize(self.tab_list[self.cur_tab].msg_as_txt))
        self.tab_list[self.cur_tab].txt_edit.setFocus()



    def send_message (self, msg_param):
        pass

    def tab_widget_changed(self):
        self.cur_tab = self.tab_widget.currentIndex()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













