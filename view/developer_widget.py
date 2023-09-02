import ctypes
import sys
import warnings

import win32gui
from PyQt5.QtCore import QRect, Qt, QCoreApplication
from PyQt5.QtGui import QIcon, QMoveEvent
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QWidget, QPushButton,
    QHBoxLayout, QGridLayout,
    QApplication,
    QMainWindow, QTabBar, QVBoxLayout, QTabWidget, QCheckBox, QLabel, QSpinBox, QLineEdit, QComboBox, QMenuBar, QMenu,
    QAction, QRadioButton, QGroupBox, QFrame,
)

from gui.gui_resources import GUIResources, GUISettings
from mathematics.vectors import Vector2i
from user_props.personal_settings import PersonalSettings
from view.gui_handler import GuiHandler


class DebugWidget(QWidget):
    def __init__(self, gui_resources: GUIResources, gui_handler: GuiHandler):
        super().__init__()
        self.gui_handler = gui_handler
        self.gui_resources = gui_resources
        self.setupUi()

    def setupUi(self):
        self.logindefaultButton = QPushButton(self)
        self.logindefaultButton.setGeometry(QRect(20, 150, 191, 61))
        self.logindefaultButton.setText("DEFAULT OBSERVING")

        self.startobservingButton = QPushButton(self)
        self.startobservingButton.setGeometry(QRect(211, 150, 191, 61))
        self.startobservingButton.setText("Start observing")

        self.stopbservingButton = QPushButton(self)
        self.stopbservingButton.setGeometry(QRect(402, 150, 191, 61))
        self.stopbservingButton.setText("Stop observing")

        self.checkbox_windows_launched = QCheckBox(self)
        self.checkbox_windows_launched.setGeometry(QRect(470, 110, 150, 17))
        self.checkbox_windows_launched.setText("Windows launched")

        # self.label = QLabel(self.centralwidget)
        # self.label.setGeometry(QRect(20, 80, 191, 31))
        # self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        # self.label.setText("Telegram ID?")

        # self.telegramID = QLineEdit(self.centralwidget)
        # self.telegramID.setGeometry(QRect(20, 110, 90, 20))

        self.windowsCount = QSpinBox(self)
        self.windowsCount.setGeometry(QRect(20, 40, 41, 22))
        self.windowsCount.setMaximum(3)
        self.windowsCount.setMinimum(1)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(20, 20, 91, 16))
        self.label_2.setText("Windows number?")

        self.launchButton = QPushButton(self)
        self.launchButton.setGeometry(QRect(110, 30, 110, 40))
        self.launchButton.setText("Launch windows")

        self.startFarm = QPushButton(self)
        self.startFarm.setGeometry(QRect(220, 30, 110, 40))
        self.startFarm.setText("Start FARM")

        self.stopFarm = QPushButton(self)
        self.stopFarm.setGeometry(QRect(330, 30, 110, 40))
        self.stopFarm.setText("Stop FARM")

        self.relaunchButton = QPushButton(self)
        self.relaunchButton.setGeometry(QRect(110, 69, 110, 40))
        self.relaunchButton.setText("Relaunch all windows")

        self.closewindowsButton = QPushButton(self)
        self.closewindowsButton.setGeometry(QRect(110, 108, 110, 40))
        self.closewindowsButton.setText("Close all windows")

        self.relogwindowsButton = QPushButton(self)
        self.relogwindowsButton.setGeometry(QRect(220, 108, 110, 40))
        self.relogwindowsButton.setText("Relog all windows")

        self.launchAndloginCharacter = QPushButton(self)
        self.launchAndloginCharacter.setGeometry(QRect(440, 30, 170, 40))
        self.launchAndloginCharacter.setText("Launch and login FROM THE LIST")

        self.connectToServerButton = QPushButton(self)
        self.connectToServerButton.setGeometry(QRect(330, 69, 110, 40))
        self.connectToServerButton.setText("Connect to server")

        self.run_server = QPushButton(self)
        self.run_server.setGeometry(QRect(330, 108, 110, 40))
        self.run_server.setText("Run Server")

        self.comboBox_accounts = QComboBox(self)
        self.comboBox_accounts.setGeometry(QRect(441, 70, 168, 20))
        self.comboBox_accounts.addItems(PersonalSettings.names)
        self.comboBox_accounts.setCurrentText(PersonalSettings.names[0])

        self.connect_all_buttons()

    def connect_all_buttons(self):
        self.launchButton.clicked.connect(lambda: self.gui_handler.launch_windows(self.windowsCount.value()))
        self.startFarm.clicked.connect(lambda: self.gui_handler.start_farm_default())
        self.stopFarm.clicked.connect(lambda: self.gui_handler.stop_bot())
        self.relaunchButton.clicked.connect(lambda: self.gui_handler.relaunch_windows())
        self.closewindowsButton.clicked.connect(lambda: self.gui_handler.close_all_windows())
        self.logindefaultButton.clicked.connect(lambda: self.gui_handler.login_default())
        self.startobservingButton.clicked.connect(lambda: self.gui_handler.start_bot())
        self.stopbservingButton.clicked.connect(lambda: self.gui_handler.stop_bot())
        self.relogwindowsButton.clicked.connect(lambda: self.gui_handler.relog_all_windows())
        self.connectToServerButton.clicked.connect(lambda: self.gui_handler.connect_to_server())
        self.run_server.clicked.connect(lambda: self.gui_handler.run_server())
        self.launchAndloginCharacter.clicked.connect(
            lambda: self.gui_handler.launch_and_login_char(self.comboBox_accounts.currentText()))

    def internet_connection_update(self, connected):
        if connected:
            self.internet_connection_label.setEnabled(True)
            self.internet_connection_label.setText("Online")
            self.internetIcon.setPixmap(QtGui.QPixmap(self.gui_resources.internet_connection_enabled_icon_path))
        else:
            self.internet_connection_label.setEnabled(False)
            self.internet_connection_label.setText("Offline")
            self.internetIcon.setPixmap(QtGui.QPixmap(self.gui_resources.internet_connection_disabled_icon_path))

