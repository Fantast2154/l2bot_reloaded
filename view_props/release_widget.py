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
    QAction, QRadioButton, QGroupBox, QFrame, QSpacerItem, QSizePolicy,
)

from gui.gui_resources import GUIResources, GUISettings
from mathematics.vectors import Vector2i
from user_props.personal_settings import PersonalSettings


class AddBotLayout(QWidget):
    def __init__(self, gui_handler):
        super().__init__()
        self.gui_handler = gui_handler

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.botGroupBox = QGroupBox()
        self.botGroupBox.setMinimumSize(QtCore.QSize(181, 200))
        self.botGroupBox.setMaximumSize(QtCore.QSize(181, 200))
        self.botGroupBox.setTitle("Bot")

        self.startBotButton = QPushButton(self.botGroupBox)
        self.startBotButton.setGeometry(QtCore.QRect(10, 110, 71, 31))
        self.startBotButton.setText("Start")

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.startBotButton.setFont(font)

        self.stopBotButton = QPushButton(self.botGroupBox)
        self.stopBotButton.setGeometry(QtCore.QRect(100, 110, 71, 31))
        self.stopBotButton.setText("Stop")

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.stopBotButton.setFont(font)

        self.botInfo = QLabel(self.botGroupBox)
        self.botInfo.setGeometry(QtCore.QRect(70, 20, 101, 51))
        self.botInfo.setText("")
        self.botInfo.setAlignment(QtCore.Qt.AlignCenter)

        self.isBroker = QRadioButton(self.botGroupBox)
        self.isBroker.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.isBroker.setText("Broker")

        self.isTrader = QRadioButton(self.botGroupBox)
        self.isTrader.setEnabled(False)
        self.isTrader.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.isTrader.setText("Trader")

        self.accountsList = QComboBox(self.botGroupBox)
        self.accountsList.setGeometry(QtCore.QRect(10, 80, 161, 21))

        self.accountsList.addItems(PersonalSettings.names)
        self.accountsList.setCurrentText(PersonalSettings.names[0])

        layout.addWidget(self.botGroupBox)

    def connect_methods_with_buttons(self):
        self.startBotButton.clicked.connect(lambda: self.gui_handler.start_bot())
        self.stopBotButton.clicked.connect(lambda: self.gui_handler.stop_bot())


class ReleaseWidget(QWidget):
    def __init__(self, gui_resources: GUIResources, gui_handler):
        super().__init__()

        self.bot_box_groups = []

        self.gui_handler = gui_handler
        self.gui_resources = gui_resources
        self.setup_ui()

    def setup_ui(self):
        horizontalLayout = QHBoxLayout()
        # internalHorizontalLayout = QHBoxLayout()

        self.add_bot_group_box(horizontalLayout)
        self.add_new_bot_button(horizontalLayout)

        horizontalLayout.addStretch()
        # horizontalLayout.addLayout(internalHorizontalLayout)

        self.setLayout(horizontalLayout)

    def add_new_bot_button(self, layout):
        addBotButton = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addBotButton.sizePolicy().hasHeightForWidth())

        addBotButton.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        addBotButton.setFont(font)
        addBotButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        addBotButton.setAutoFillBackground(False)
        addBotButton.setText('')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.gui_resources.plus_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        addBotButton.setIcon(icon)
        addBotButton.setIconSize(QtCore.QSize(75, 75))
        layout.addWidget(addBotButton)
        # self.externalHorizontalLayout.addWidget(self.addBotButton)

        # spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.externalHorizontalLayout.addItem(spacerItem)

        addBotButton.clicked.connect(lambda: self.add_bot_group_box_click(layout))

    def add_bot_group_box(self, layout):
        a = AddBotLayout(self.gui_handler)
        layout.insertWidget(len(layout) - 3, a)
        # layout.addWidget(a)
        self.bot_box_groups.append(a)

    def add_bot_group_box_click(self, layout):
        self.add_bot_group_box(layout)

    def send_message(self, message):
        temp = 'View' + ': ' + message
        print(temp)
