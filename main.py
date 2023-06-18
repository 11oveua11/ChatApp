import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *
from tabs import *
import client
import socket
from threading import Thread

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ChatApp!')
        self.resize(400, 400)
        # self.move(100, 100)
        self.setWindowIcon(QIcon('icon1.png'))

        # self.message = AdvMessage()
        # self.msg_as_txt_0 = ""
        self.tab_widget = QTabWidget(self)
        self.cur_tab = 0                    # Index of active tab widget
        self.tab_list = []                  # List of tabs(Qwidget) for tab_widget(QTabWidget)
        self.emoji_list = []
        for i in range(128512, 128592):
            self.emoji_list.append(chr(i))

        self.tab_list.append(Tab())
        self.tab_widget.currentChanged.connect(self.tab_widget_changed)
        self.tab_widget.addTab(self.tab_list[0], "Tab 0")

        self.vbox_main_layout = QVBoxLayout(self)
        self.vbox_main_layout.setContentsMargins(0, 0, 0, 0)
        self.vbox_main_layout.addWidget(self.tab_widget)


        self.hbox_layout = QHBoxLayout(self)
        self.hbox_layout.setContentsMargins(0, 0, 0, 0)

        self.btn_send = QPushButton(self)
        # self.btnSend.move(360, 300)
        # self.btnSend.resize(40, 40)
        self.btn_send.clicked.connect(self.btnSend_clicked)
        self.btn_send.setIcon(QIcon('send-icon.png'))

        self.btn_additions = QPushButton(self)
        # self.btnAdditions.move(360, 340)
        # self.btnAdditions.resize(40, 40)
        self.btn_additions.clicked.connect(self.btnAdditions_clicked)
        self.btn_additions.setIcon(QIcon('emoji-icon.png'))

        self.emoji_qwidget = QWidget(self)
        self.emoji_qwidget.setWindowFlags(Qt.Popup)
        self.emoji_qwidget.resize(242, 292)

        self.emoji_txt_browser = QTextBrowser(self.emoji_qwidget)
        self.emoji_txt_browser.resize(242, 292)
        self.emoji_txt_browser.setText(self.emoji_to_html(self.emoji_list))
        self.emoji_txt_browser.setOpenLinks(False)
        self.emoji_txt_browser.anchorClicked.connect(self.emoji_link_clicked)

        # emoji_txt_browser.setHidden(True)

        self.btn_temp = QPushButton("новый чат", self)
        self.btn_temp.clicked.connect(self.btn_temp_method)

        self.hbox_layout.addWidget(self.btn_send)
        self.hbox_layout.addWidget(self.btn_additions)
        self.hbox_layout.addWidget(self.btn_temp)

        self.vbox_main_layout.addLayout(self.hbox_layout)



    def btn_temp_method(self):
        tr1 = Thread(target=self.client_server)
        tr1.start()



        # self.tab_list[self.cur_tab].txt_browser.append(self.my_client.get_request_data())
        # add_new_tab
        # self.tab_list.append(Tab())
        # self.tab_widget.addTab(self.tab_list[-1], "Tab " + str(len(self.tab_list) - 1))

    def client_server(self):
        self.s_clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_clnt.connect(('127.0.0.1', 1234))
        self.s_clnt.send(bytes('new_user Sam qwerty321 1', 'utf-8'))
        msg = True
        while True and msg!='':
            msg = self.s_clnt.recv(1024)
            if not msg:
                break
            print(msg.decode('utf-8'))


    def btnSend_clicked(self):
        # self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()
        self.tab_list[self.cur_tab].txt_browser.append(emoji.emojize(self.tab_list[self.cur_tab].msg_as_txt))
        self.tab_list[self.cur_tab].txt_edit.clear()
        self.tab_list[self.cur_tab].txt_edit.setFocus()

    def btnAdditions_clicked(self):

        # print(self.pos())
        # print(self.btn_additions.pos())
        self.emoji_qwidget.move(self.btn_additions.pos() + self.pos() + QPoint(0, 30))
        # print(self.emoji_qwidget.pos())
        self.emoji_qwidget.show()

    def emoji_link_clicked(self, qurl):

        # print(int(qurl.toString()))
        # print(emoji.emojize("".join(self.emoji_list)))
        self.tab_list[self.cur_tab].msg_as_txt = self.tab_list[self.cur_tab].txt_edit.toPlainText() + self.emoji_list[int(qurl.toString())]
        self.tab_list[self.cur_tab].txt_edit.setText(emoji.emojize(self.tab_list[self.cur_tab].msg_as_txt))
        self.tab_list[self.cur_tab].txt_edit.setFocus()



    def send_message (self, msg_param):
        pass

    def tab_widget_changed(self):
        self.cur_tab = self.tab_widget.currentIndex()

    def emoji_to_html(self, emoji_list):
#         main_txt = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
# <html><head><meta name="qrichtext" content="1" /><style type="text/css">
# p, li { white-space: pre-wrap; }
# </style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
# """
        main_txt = ''
        a1 = """<a href='"""
        a2 = """' style='text-decoration: none' >"""
        a3 = """</a>"""
        for em in emoji_list:
            main_txt = main_txt + (a1 + str(emoji_list.index(em)) + a2 + em + a3)
        return '''<body style="font-size: 16pt;">''' + main_txt + '''</body>'''



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













