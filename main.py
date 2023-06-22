import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Msg import *
from tabs import *
from config import *
import client
import socket
from threading import Thread

class DlgMain(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('ChatApp!')
        self.resize(400, 500)
        # self.move(100, 100)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, True)
        self.setWindowIcon(QIcon('icon.png'))

        self.server = ''
        self.port = None
        self.load_btn_clicked()


        # self.message = AdvMessage()
        # self.msg_as_txt_0 = ""
        self.answer = ''
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

        self.btn_send = QPushButton(" Send", self)
        # self.btn_send.setContentsMargins(0, 0, 0, 0)
        self.btn_send.clicked.connect(self.btn_send_clicked)
        self.btn_send.setIcon(QIcon('icon.png'))

        self.btn_emoji = QPushButton(" Emoji", self)
        self.btn_emoji.setContentsMargins(0, 0, 0, 0)
        self.btn_emoji.clicked.connect(self.btn_emoji_clicked)
        self.btn_emoji.setIcon(QIcon('icon-emoji.png'))

        self.btn_settings = QPushButton(" Settings", self)
        self.btn_settings.setContentsMargins(0, 0, 0, 0)
        self.btn_settings.clicked.connect(self.btn_settings_clicked)
        self.btn_settings.setIcon(QIcon('icon-settings.png'))

        self.btn_temp = QPushButton("test func", self)
        self.btn_temp.setContentsMargins(0, 0, 0, 0)
        self.btn_temp.clicked.connect(self.btn_temp_clicked)

        self.emoji_qwidget = QWidget(self)
        self.emoji_qwidget.setWindowFlags(Qt.Popup)
        self.emoji_qwidget.resize(242, 292)

        self.emoji_txt_browser = QTextBrowser(self.emoji_qwidget)
        self.emoji_txt_browser.resize(242, 292)
        self.emoji_txt_browser.setText(self.emoji_to_html(self.emoji_list))
        self.emoji_txt_browser.setOpenLinks(False)
        self.emoji_txt_browser.anchorClicked.connect(self.emoji_link_clicked)
        # emoji_txt_browser.setHidden(True)

        self.hbox_layout.addWidget(self.btn_send)
        self.hbox_layout.addWidget(self.btn_emoji)
        self.hbox_layout.addWidget(self.btn_settings)
        self.hbox_layout.addWidget(self.btn_temp)

        self.status_bar = QStatusBar(self)


        self.vbox_main_layout.addLayout(self.hbox_layout)
        self.vbox_main_layout.addWidget(self.status_bar)
        self.setLayout(self.vbox_main_layout)


        self.settings_widget = QWidget(flags=Qt.MSWindowsFixedSizeDialogHint)
        # self.settings_widget.setWindowFlag(Qt.FramelessWindowHint)
        self.settings_widget.resize(400, 400)
        self.settings_widget.move(200, 200)
        # self.settings_widget.

        self.vbox_settings = QVBoxLayout(self.settings_widget)
        self.group_podkluchenie = QGroupBox("Подключение", self.settings_widget)
        self.group_podkluchenie.setGeometry(10, 10, 380, 50)
        self.hbox_podkluchenie = QHBoxLayout(self.settings_widget)
        self.group_podkluchenie.setLayout(self.hbox_podkluchenie)
        self.set_server = QLineEdit(self.group_podkluchenie)
        # self.set_server.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=2))
        self.set_server.resize(80, 20)
        self.set_server.setPlaceholderText("сервер")
        self.set_port = QLineEdit(self.group_podkluchenie)
        # self.set_port.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=1))
        self.set_port.resize(30, 20)
        self.set_port.setPlaceholderText("порт")
        # self.set_port.setWindowFlag(Qt.)
        self.set_test_button = QPushButton("TEST", self.settings_widget)
        self.set_test_button.clicked.connect(self.set_test_button_click)
        self.hbox_podkluchenie.setContentsMargins(4, 0, 4, 0)
        self.hbox_podkluchenie.minimumSize()
        self.hbox_podkluchenie.addWidget(self.set_server)
        self.hbox_podkluchenie.addWidget(self.set_port)
        self.hbox_podkluchenie.addWidget(self.set_test_button)


        self.group_reg = QGroupBox("Регистрация пользователя", self.settings_widget)
        self.group_reg.setGeometry(10, 10, 380, 50)
        self.hbox_reg = QHBoxLayout(self.settings_widget)
        self.group_reg.setLayout(self.hbox_reg)
        self.set_login = QLineEdit(self.group_reg)
        # self.set_server.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=2))
        self.set_login.resize(80, 20)
        self.set_login.setPlaceholderText("сервер")
        self.set_pass = QLineEdit(self.group_reg)
        # self.set_port.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=1))
        self.set_pass.resize(30, 20)
        self.set_pass.setPlaceholderText("порт")
        # self.set_port.setWindowFlag(Qt.)
        self.set_reg_button = QPushButton("TEST", self.settings_widget)
        self.set_reg_button.clicked.connect(self.set_reg_button_click)
        self.hbox_reg.setContentsMargins(4, 0, 4, 0)
        self.hbox_reg.minimumSize()
        self.hbox_reg.addWidget(self.set_login)
        self.hbox_reg.addWidget(self.set_pass)
        self.hbox_reg.addWidget(self.set_reg_button)

        self.group_buttons = QGroupBox(self.settings_widget)
        self.group_buttons.setGeometry(10, 10, 380, 50)
        self.hbox_buttons = QHBoxLayout(self.settings_widget)
        self.group_buttons.setLayout(self.hbox_buttons)
        self.load_btn = QPushButton('Load settings', self.group_buttons)
        self.load_btn.clicked.connect(self.load_btn_clicked)
        # self.set_server.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=2))
        # self.set_login.resize(80, 20)

        self.save_btn = QPushButton('Save settings', self.group_buttons)
        self.save_btn.clicked.connect(self.save_btn_clicked)
        # self.set_port.setSizePolicy(QSizePolicy.setHorizontalStretch(stretchFactor=1))
        # self.set_pass.resize(30, 20)
        self.hbox_buttons.addWidget(self.load_btn)
        self.hbox_buttons.addWidget(self.save_btn)

        self.vbox_settings.addWidget(self.group_podkluchenie)
        self.vbox_settings.addWidget(self.group_reg)
        self.verticalSpacer = QSpacerItem(20, 200)
        self.vbox_settings.addItem(self.verticalSpacer)
        self.vbox_settings.addWidget(self.group_buttons)




        self.settings_widget.show()

    # def client_server(self, arg):
    #     self.cl = client.Client()
    #     self.cl.get_request_data(self, arg)


    def btn_send_clicked(self):
        # self.hist_text = self.hist_text + '\n\n' + self.txtEdit.toPlainText()
        self.tab_list[self.cur_tab].txt_browser.append(emoji.emojize(self.tab_list[self.cur_tab].msg_as_txt))
        self.tab_list[self.cur_tab].txt_edit.clear()
        self.tab_list[self.cur_tab].txt_edit.setFocus()

    def btn_emoji_clicked(self):

        # print(self.pos())
        # print(self.btn_additions.pos())
        self.emoji_qwidget.move(self.btn_emoji.pos() + self.pos() + QPoint(0, 30))
        # print(self.emoji_qwidget.pos())
        self.emoji_qwidget.show()

    def btn_settings_clicked(self):
        # self.settings_widget.setWindowFlags(Qt.Popup)
        self.settings_widget.show()

    def btn_temp_clicked(self):
        pass
        tr1 = Thread(target=self.thread_client_server)
        tr1.start()



        # self.tab_list[self.cur_tab].txt_browser.append(self.my_client.get_request_data())
        # add_new_tab
        # self.tab_list.append(Tab())
        # self.tab_widget.addTab(self.tab_list[-1], "Tab " + str(len(self.tab_list) - 1))


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

    def set_test_button_click(self):
        answer = self.cl.get_request_data('test')
        if answer.decode('utf-8') == 'True':
            self.set_test_button.setStyleSheet('QPushButton {background-color: #00C100}')
            self.set_test_button.setText('+WORKS+')

    def thread_client_server(self):
        cl = client.Client()
        ans = cl.get_request_data('new_user', 'Jim', 'q1w2e3r4', '1')
        print(ans)

    def thread_function(self):
        pass


    def set_reg_button_click(self):
        pass

    def load_btn_clicked(self):
        self.server = conf['server']
        self.port = conf['port']

    def save_btn_clicked(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())













