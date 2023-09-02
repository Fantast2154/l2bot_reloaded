import threading
import time

import win32gui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from user_props.personal_settings import PersonalSettings

class WindowUI(object):
    def __init__(self, MainWindow, gui_handler):
        self.window_name = 'baganec & germanec'
        self.is_running = False
        self.main_window = MainWindow
        self.gui_handler = gui_handler

        self.bot_box_groups = []

        self._translate = QtCore.QCoreApplication.translate
        self.setupUi(MainWindow)

    def send_message(self, message):
        print('{}: {}'.format(self.__class__.__name__, f'{message}'))



    def setupUi(self, MainWindow):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/qtfiles/fishing.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logindefaultButton = QtWidgets.QPushButton(self.centralwidget)
        self.logindefaultButton.setGeometry(QtCore.QRect(20, 150, 191, 61))
        self.logindefaultButton.setObjectName("logindefaultButton")
        self.startobservingButton = QtWidgets.QPushButton(self.centralwidget)
        self.startobservingButton.setGeometry(QtCore.QRect(211, 150, 191, 61))
        self.startobservingButton.setObjectName("startobservingButton")
        self.stopbservingButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbservingButton.setGeometry(QtCore.QRect(402, 150, 191, 61))
        self.stopbservingButton.setObjectName("stopbservingButton")

        self.checkbox_windows_launched = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_windows_launched.setGeometry(QtCore.QRect(550, 110, 101, 17))
        self.checkbox_windows_launched.setObjectName("checkbox_count_particles")

        self.internetIcon = QtWidgets.QLabel(self.centralwidget)
        self.internetIcon.setGeometry(QtCore.QRect(12, 8, 15, 15))
        self.internetIcon.setText("")
        self.internetIcon.setPixmap(QtGui.QPixmap("gui/qtfiles/offline380x380.png"))
        self.internetIcon.setScaledContents(True)
        self.internetIcon.setObjectName("internetIcon")
        self.internet_connection_label = QtWidgets.QLabel(self.centralwidget)
        self.internet_connection_label.setEnabled(False)
        self.internet_connection_label.setGeometry(QtCore.QRect(28, 8, 47, 13))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 191, 31))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.telegramID = QtWidgets.QLineEdit(self.centralwidget)
        self.telegramID.setGeometry(QtCore.QRect(20, 110, 191, 20))
        self.telegramID.setObjectName("telegramID")
        self.windowsCount = QtWidgets.QSpinBox(self.centralwidget)
        self.windowsCount.setGeometry(QtCore.QRect(20, 40, 41, 22))
        self.windowsCount.setObjectName("windowsCount")
        self.windowsCount.setMaximum(3)
        self.windowsCount.setMinimum(1)
        self.windowsCount.setObjectName("windowsCount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setGeometry(QtCore.QRect(110, 30, 110, 40))
        self.launchButton.setObjectName("relaunchButton")
        self.startFarm = QtWidgets.QPushButton(self.centralwidget)
        self.startFarm.setGeometry(QtCore.QRect(220, 30, 110, 40))
        self.startFarm.setObjectName("startFarmButton")
        self.stopFarm = QtWidgets.QPushButton(self.centralwidget)
        self.stopFarm.setGeometry(QtCore.QRect(330, 30, 110, 40))
        self.stopFarm.setObjectName("startFarmButton")
        # self.logindefaultButton = QtWidgets.QPushButton(self.centralwidget)
        # self.logindefaultButton.setGeometry(QtCore.QRect(220, 30, 110, 40))
        # self.logindefaultButton.setObjectName("logindefaultButton")
        self.relaunchButton = QtWidgets.QPushButton(self.centralwidget)
        self.relaunchButton.setGeometry(QtCore.QRect(110, 69, 110, 40))
        self.relaunchButton.setObjectName("connectWindows")
        # self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        # self.connectButton.setGeometry(QtCore.QRect(220, 69, 110, 40))
        # self.connectButton.setObjectName("cconnectWindows")
        self.closewindowsButton = QtWidgets.QPushButton(self.centralwidget)
        self.closewindowsButton.setGeometry(QtCore.QRect(110, 108, 110, 40))
        self.closewindowsButton.setObjectName("closeWindows")
        self.relogwindowsButton = QtWidgets.QPushButton(self.centralwidget)
        self.relogwindowsButton.setGeometry(QtCore.QRect(220, 108, 110, 40))
        self.relogwindowsButton.setObjectName("relogwindowsButton")

        self.launchAndloginCharacter = QtWidgets.QPushButton(self.centralwidget)
        self.launchAndloginCharacter.setGeometry(QtCore.QRect(440, 20, 170, 40))
        self.launchAndloginCharacter.setObjectName("launchAndloginCharacter")

        self.connectToServerButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectToServerButton.setGeometry(QtCore.QRect(330, 69, 110, 40))
        self.connectToServerButton.setObjectName("connectToServer")

        self.run_server = QtWidgets.QPushButton(self.centralwidget)
        self.run_server.setGeometry(QtCore.QRect(330, 108, 110, 40))
        self.run_server.setObjectName("run_server")

        self.comboBox_accounts = QtWidgets.QComboBox(MainWindow)
        self.comboBox_accounts.setGeometry(QtCore.QRect(440, 80, 140, 20))
        self.comboBox_accounts.setObjectName("comboBox_accounts")
        self.comboBox_accounts.addItems(PersonalSettings.names)
        # for _ in PersonalSettings.names:
        #     self.comboBox_accounts.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 227, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionHow_to_botovodit_GUIDE = QtWidgets.QAction(MainWindow)
        self.actionHow_to_botovodit_GUIDE.setObjectName("actionHow_to_botovodit_GUIDE")
        self.menuHelp.addAction(self.actionHow_to_botovodit_GUIDE)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.startobservingButton.clicked.connect(lambda: self.start_observing())
        self.launchButton.clicked.connect(lambda: self.gui_handler.launch_windows(self.windowsCount.value()))
        self.startFarm.clicked.connect(lambda: self.gui_handler.start_farm_default())
        self.stopFarm.clicked.connect(lambda: self.gui_handler.stop_bot())
        self.relaunchButton.clicked.connect(lambda: self.gui_handler.relaunch_windows())
        self.closewindowsButton.clicked.connect(lambda: self.gui_handler.close_all_windows())
        self.logindefaultButton.clicked.connect(lambda: self.gui_handler.login_default())
        # self.connectButton.clicked.connect(lambda: self.gui_handler.connect_windows())
        self.startobservingButton.clicked.connect(lambda: self.gui_handler.start_bot())
        self.stopbservingButton.clicked.connect(lambda: self.gui_handler.stop_bot())
        self.relogwindowsButton.clicked.connect(lambda: self.gui_handler.relog_all_windows())
        self.connectToServerButton.clicked.connect(lambda: self.gui_handler.connect_to_server())
        self.run_server.clicked.connect(lambda: self.gui_handler.run_server())
        self.launchAndloginCharacter.clicked.connect(lambda: self.gui_handler.launch_and_login_char(self.comboBox_accounts.currentText()))

    def internet_connection_update(self, connected):
        if connected:
            self.internet_connection_label.setEnabled(True)
            self.internet_connection_label.setText("Online")
            self.internetIcon.setPixmap(QtGui.QPixmap("view/qtfiles/online380x380.png"))
        else:
            self.internet_connection_label.setEnabled(False)
            self.internet_connection_label.setText("Offline")
            self.internetIcon.setPixmap(QtGui.QPixmap("view/qtfiles/offline380x380.png"))

    # def start(self):
    #     t = threading.Thread(target=self._run())
    #     self.is_running = True
    #     t.start()
    #
    # def stop(self):
    #     self.is_running = False

    # def _run(self):
    #     while self.is_running:
    #         pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self.window_name))
        self.startobservingButton.setText(_translate("MainWindow", "Start observing"))
        self.stopbservingButton.setText(_translate("MainWindow", "Stop observing"))
        self.label.setText("Telegram ID?")
        self.label_2.setText(_translate("MainWindow", "Windows number?"))
        self.launchButton.setText(_translate("MainWindow", "Launch windows"))
        self.startFarm.setText(_translate("MainWindow", "Start FARM"))
        self.stopFarm.setText(_translate("MainWindow", "Stop FARM"))
        self.checkbox_windows_launched.setText(_translate("MainWindow", "Windows launched"))
        self.logindefaultButton.setText(_translate("MainWindow", "DEFAULT OBSERVING"))
        self.relaunchButton.setText(_translate("MainWindow", "Relaunch all windows"))
        self.relogwindowsButton.setText(_translate("MainWindow", "Relog all windows"))
        self.closewindowsButton.setText(_translate("MainWindow", "Close all windows"))
        # self.connectButton.setText(_translate("MainWindow", "Connect windows"))
        self.launchAndloginCharacter.setText(_translate("MainWindow", "Launch and login FROM THE LIST"))
        self.connectToServerButton.setText(_translate("MainWindow", "Connect to server"))
        self.run_server.setText(_translate("MainWindow", "Run Server"))
        self.internet_connection_label.setText(self._translate("MainWindow", "Offline"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHow_to_botovodit_GUIDE.setText(_translate("MainWindow", "How to botovodit`. GUIDE"))

        self.comboBox_accounts.setCurrentText(_translate("MainWindow", PersonalSettings.names[0]))

        # def init_account_groupbox():
        #     for i, name in enumerate(PersonalSettings.names):
        #         self.comboBox_accounts.setItemText(i, _translate("MainWindow", name))
        #
        # init_account_groupbox()


class View(WindowUI):
    def __init__(self, gui_handler):
        self.send_message('created')
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.gui_handler = gui_handler
        self.width = 630
        self.height = 253

        self.left_top_x = 600
        self.left_top_y = 792
        super(View, self).__init__(self.MainWindow, self.gui_handler)
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(self.width, self.height)
        self.MainWindow.setMinimumSize(QtCore.QSize(self.width, self.height))
        self.MainWindow.setMaximumSize(QtCore.QSize(self.width, self.height))
        self.MainWindow.move(self.left_top_x, self.left_top_y)
        self.MainWindow.show()


    def send_message(self, message):
        print('{}: {}'.format(self.__class__.__name__, f'{message}'))


if __name__ == "__main__":
    v = View(None)
    sys.exit(v.app.exec_())
