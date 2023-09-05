import ctypes
import random
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
    QAction, QRadioButton, QGroupBox, QFrame, QSpacerItem, QSizePolicy, QLayout,
)

from gui.gui_resources import GUIResources, GUISettings
from mathematics.vectors import Vector2i
from user_props.personal_settings import PersonalSettings


class AddBotLayout(QWidget):
    def __init__(self, gui_resources: GUIResources, gui_handler, parent_widget):
        super().__init__()
        self.gui_handler = gui_handler
        self.gui_resources = gui_resources

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        botGroupBox = QGroupBox()

        vertical_layout = QVBoxLayout()
        vertical_layout.setContentsMargins(0, 0, 0, 0)

        botGroupBox.setMinimumSize(QtCore.QSize(181, 200))
        botGroupBox.setMaximumSize(QtCore.QSize(181, 200))
        botGroupBox.setTitle("Bot")

        startBotButton = QPushButton()
        startBotButton.setIcon(QIcon(self.gui_resources.start_icon))
        startBotButton.setIconSize(QtCore.QSize(25, 25))
        startBotButton.setFixedSize(35, 35)
        startBotButton.setFlat(True)
        startBotButton.setToolTip('Start bot')

        pauseBotButton = QPushButton()
        pauseBotButton.setIcon(QIcon(self.gui_resources.pause_icon))
        pauseBotButton.setIconSize(QtCore.QSize(25, 25))
        pauseBotButton.setFixedSize(35, 35)
        pauseBotButton.setFlat(True)
        pauseBotButton.setToolTip('Pause bot')

        stopBotButton = QPushButton()
        stopBotButton.setIcon(QIcon(self.gui_resources.stop_icon))
        stopBotButton.setIconSize(QtCore.QSize(25, 25))
        stopBotButton.setFixedSize(35, 35)
        stopBotButton.setFlat(True)
        stopBotButton.setToolTip('Stop bot')

        delete_bot_button = QPushButton()
        delete_bot_button.setIcon(QIcon(self.gui_resources.delete_icon))
        delete_bot_button.setFixedSize(35, 35)
        delete_bot_button.setIconSize(QtCore.QSize(35, 35))
        delete_bot_button.setFlat(True)
        delete_bot_button.setToolTip('Удалить бота')
        delete_bot_button.clicked.connect(lambda: parent_widget.delete_bot(self))

        switch_button = QPushButton()
        switch_button.setIcon(QIcon(self.gui_resources.switch_icon))
        switch_button.setFixedSize(35, 35)
        switch_button.setIconSize(QtCore.QSize(35, 35))
        switch_button.setFlat(True)
        switch_button.setToolTip('Сменить роль у бота. Например, рыбака на трейдера; рб-тракера на фармера и пр.')

        internetIcon = QLabel()
        internetIcon.setFixedSize(20, 20)
        internetIcon.setText('')
        internetIcon.setToolTip('Bot is inactive')
        internetIcon.setPixmap(QtGui.QPixmap(self.gui_resources.inactive_icon))
        internetIcon.setScaledContents(True)

        accountsList = QComboBox()
        accountsList.setGeometry(QtCore.QRect(10, 80, 161, 21))
        accountsList.setToolTip('Список аккаунтов. Потом сделаем так, чтобы можно было выбирать только лишь из '
                                'незанятых акков')

        accountsList.addItems(PersonalSettings.names)
        accountsList.setCurrentText(PersonalSettings.names[0])
        # internal_layout.addWidget(accountsList)

        status_characters_list_HLayout = QHBoxLayout(botGroupBox)
        status_characters_list_HLayout.addWidget(internetIcon)
        status_characters_list_HLayout.addWidget(accountsList)
        status_characters_list_HLayout.setContentsMargins(0, 0, 0, 0)
        status_characters_list_HLayout.setSpacing(0)

        status_characters_list_widget = QWidget()
        status_characters_list_widget.setLayout(status_characters_list_HLayout)
        status_characters_list_widget.setContentsMargins(0, 0, 0, 0)

        controlsLayout = QHBoxLayout(botGroupBox)
        controlsLayout.setAlignment(Qt.AlignHCenter)
        controlsLayout.setContentsMargins(0, 0, 0, 0)
        controlsLayout.setSpacing(0)
        controlsLayout.addWidget(startBotButton)
        controlsLayout.addWidget(pauseBotButton)
        controlsLayout.addWidget(stopBotButton)
        # s2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # controlsLayout.addSpacerItem(s2)
        # controlsLayout.addStretch()

        controls_widget = QWidget()
        controls_widget.setLayout(controlsLayout)
        controls_widget.setContentsMargins(0, 0, 0, 0)

        delete_switch_h_layout = QHBoxLayout(botGroupBox)
        delete_switch_h_layout.addWidget(delete_bot_button, alignment=Qt.AlignLeft)
        delete_switch_h_layout.addWidget(switch_button, alignment=Qt.AlignRight)

        delete_switch_widget = QWidget(botGroupBox)
        delete_switch_widget.setLayout(delete_switch_h_layout)

        vertical_layout.addWidget(delete_switch_widget)
        # vertical_layout.addWidget(switch_button, alignment=Qt.AlignRight)

        # test_grid.addWidget(b3, alignment=Qt.AlignTop)
        # test_grid.addWidget(b4, alignment=Qt.AlignTop)

        grid = QGridLayout(botGroupBox)
        grid_widget = QWidget(botGroupBox)
        grid_widget.setLayout(grid)
        r = self.gui_resources
        icons = [r.internet_connection_disabled_icon_path,
                 r.internet_connection_enabled_icon_path,
                 ]

        for i in range(4):
            for j in range(random.randint(3, 7)):
                test_button = QPushButton()
                # test_button = QLabel()
                test_button.setText('')
                test_button.setFlat(True)
                # test_button.setScaledContents(True)
                test_button.setFixedSize(15, 15)
                test_button.setToolTip('Тут будут бафы')
                test_button.setIcon(QIcon(icons[random.randint(0, len(icons) - 1)]))
                # test_button.setPixmap(QtGui.QPixmap(icons[random.randint(0, len(icons) - 1)]))
                grid.addWidget(test_button, i, j)

        grid.setAlignment(Qt.AlignLeft)
        grid.setSpacing(0)
        grid.setContentsMargins(0, 0, 0, 0)

        kill_icon = QLabel()
        kill_icon.setText('')
        kill_icon.setScaledContents(True)
        kill_icon.setFixedSize(25, 25)
        kill_icon.setToolTip('Количество убитых мобов')
        kill_icon.setPixmap(QtGui.QPixmap(self.gui_resources.kill_icon))

        text = ['1917', '0', '1237', '9999999']
        kill_text = QLabel()
        kill_text.setText(text[random.randint(0, len(text) - 1)])
        kill_text.setScaledContents(True)
        kill_text.setFixedSize(55, 10)
        kill_text.setToolTip('Количество убитых мобов')

        # grid.addWidget(kill_icon, 4, 0, 1, 3)
        kill_h_box_layout = QHBoxLayout(botGroupBox)

        kill_h_box_layout.addWidget(kill_icon)
        kill_h_box_layout.addWidget(kill_text)

        kill_h_box_layout.setAlignment(Qt.AlignLeft)
        kill_h_box_layout.setContentsMargins(0, 0, 0, 0)
        kill_h_box_layout.setSpacing(0)

        kills_widget = QWidget()
        kills_widget.setLayout(kill_h_box_layout)
        kills_widget.setContentsMargins(0, 0, 0, 0)

        t = QHBoxLayout(botGroupBox)
        t.addWidget(grid_widget)
        t_widget = QWidget()
        t_widget.setMinimumSize(100, 70)
        t_widget.setLayout(t)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(0)
        vertical_layout.addWidget(status_characters_list_widget, alignment=Qt.AlignTop)
        vertical_layout.addWidget(t_widget, alignment=Qt.AlignTop)
        vertical_layout.addWidget(kills_widget, alignment=Qt.AlignTop)
        vertical_layout.addWidget(controls_widget, alignment=Qt.AlignTop)
        # vertical_layout.addStretch()
        # test_grid.addWidget(switch_button, 0, 0, 1, 3, alignment=Qt.AlignLeft)
        # test_grid.addWidget(status_characters_list_widget, 1, 0, 1, 3)
        # test_grid.setAlignment(switch_button, Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addLayout(vertical_layout)
        # layout.addWidget(botGroupBox)

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
        self.horizontalLayout = QHBoxLayout()
        # internalHorizontalLayout = QHBoxLayout()

        self.add_bot_group_box(self.horizontalLayout)
        self.add_new_bot_button(self.horizontalLayout)

        self.horizontalLayout.addStretch()
        # horizontalLayout.addLayout(internalHorizontalLayout)

        self.setLayout(self.horizontalLayout)

    def add_new_bot_button(self, layout):
        self.addBotButton = QPushButton()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBotButton.sizePolicy().hasHeightForWidth())
        self.addBotButton.setToolTip('Добавить бота')
        self.addBotButton.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        self.addBotButton.setFont(font)
        self.addBotButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addBotButton.setAutoFillBackground(False)
        self.addBotButton.setText('')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.gui_resources.plus_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.addBotButton.setIcon(icon)
        self.addBotButton.setIconSize(QtCore.QSize(75, 75))
        self.addBotButton.setFlat(True)
        layout.addWidget(self.addBotButton)
        # self.externalHorizontalLayout.addWidget(self.addBotButton)

        # spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.externalHorizontalLayout.addItem(spacerItem)

        self.addBotButton.clicked.connect(lambda: self.add_bot_group_box(layout))

    def add_bot_group_box(self, layout):
        a = AddBotLayout(self.gui_resources, self.gui_handler, self)
        if len(layout) == 1:
            layout.insertWidget(len(layout) - 3, a)
        else:
            layout.insertWidget(len(layout) - 2, a)
        # layout.addWidget(a)
        self.bot_box_groups.append(a)
        if len(self.bot_box_groups) == 3:
            self.addBotButton.setHidden(True)

    def delete_bot(self, widget):
        pass
        # self.horizontalLayout.removeWidget(widget)
        # self.bot_box_groups.remove(widget)
        #self.send_message('DELETE BOT')

    def send_message(self, message):
        temp = 'View' + ': ' + message
        print(temp)
