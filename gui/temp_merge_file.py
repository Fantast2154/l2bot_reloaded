from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class WindowUI(object):
    def __init__(self, MainWindow, controller):
        self.main_window = MainWindow
        self.controller = controller

        self.bot_box_groups = []

        self._translate = QtCore.QCoreApplication.translate
        self.setup_ui(MainWindow)

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(558, 194)
        MainWindow.setWindowIcon(QtGui.QIcon("gui/icons/header_icon380x380.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-9, 137, 101, 41))
        self.frame.setObjectName("frame")
        self.db_status_icon = QtWidgets.QLabel(self.frame)
        self.db_status_icon.setGeometry(QtCore.QRect(12, 18, 15, 15))
        self.db_status_icon.setText("")
        self.db_status_icon.setPixmap(QtGui.QPixmap("gui/icons/offline380x380.png"))
        self.db_status_icon.setScaledContents(True)
        self.db_status_icon.setObjectName("db_status_icon")
        self.db_status_label = QtWidgets.QLabel(self.frame)
        self.db_status_label.setEnabled(False)
        self.db_status_label.setGeometry(QtCore.QRect(22, 18, 47, 13))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.db_status_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.db_status_label.setFont(font)
        self.db_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_status_label.setObjectName("db_status_label")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 711, 155))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.externalHorizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.externalHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.externalHorizontalLayout.setObjectName("externalHorizontalLayout")
        self.internalHorizontalLayout = QtWidgets.QHBoxLayout()
        self.internalHorizontalLayout.setObjectName("internalHorizontalLayout")

        self.add_bot_group_box(self.horizontalLayoutWidget_2, self.internalHorizontalLayout)

        self.externalHorizontalLayout.addLayout(self.internalHorizontalLayout)

        self.add_new_bot_button()

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFishers = QtWidgets.QMenu(self.menubar)
        self.menuFishers.setObjectName("menuFishers")
        MainWindow.setMenuBar(self.menubar)
        self.actionPrivet = QtWidgets.QAction(MainWindow)
        self.actionPrivet.setObjectName("actionPrivet")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.actionContact_Baganec = QtWidgets.QAction(MainWindow)
        self.actionContact_Baganec.setObjectName("actionContact_Baganec")
        self.actionContact_Germanec = QtWidgets.QAction(MainWindow)
        self.actionContact_Germanec.setObjectName("actionContact_Germanec")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_fisher = QtWidgets.QAction(MainWindow)
        self.actionNew_fisher.setEnabled(False)
        self.actionNew_fisher.setObjectName("actionNew_fisher")
        self.actionNew_supplier = QtWidgets.QAction(MainWindow)
        self.actionNew_supplier.setEnabled(False)
        self.actionNew_supplier.setObjectName("actionNew_supplier")
        self.actionNew_farmer = QtWidgets.QAction(MainWindow)
        self.actionNew_farmer.setEnabled(False)
        self.actionNew_farmer.setObjectName("actionNew_farmer")
        self.actionNew_observer = QtWidgets.QAction(MainWindow)
        self.actionNew_observer.setEnabled(False)
        self.actionNew_observer.setObjectName("actionNew_observer")

        self.menuFile.addAction(self.actionPrivet)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.menuHelp.addAction(self.actionContact_Baganec)
        self.menuHelp.addAction(self.actionContact_Germanec)
        self.menuHelp.addAction(self.actionAbout)

        self.menuFishers.addAction(self.actionNew_fisher)
        self.menuFishers.addAction(self.actionNew_supplier)
        self.menuFishers.addAction(self.actionNew_farmer)
        self.menuFishers.addAction(self.actionNew_observer)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFishers.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_new_bot_button(self):
        self.addBotButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBotButton.sizePolicy().hasHeightForWidth())
        self.addBotButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.addBotButton.setFont(font)
        self.addBotButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addBotButton.setAutoFillBackground(False)
        self.addBotButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBotButton.setIcon(icon)
        self.addBotButton.setIconSize(QtCore.QSize(75, 75))
        self.addBotButton.setObjectName("addBotButton")
        self.externalHorizontalLayout.addWidget(self.addBotButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.externalHorizontalLayout.addItem(spacerItem)

        self.addBotButton.clicked.connect(lambda: self.add_bot_group_box_click(self.horizontalLayoutWidget_2,
                                                                               self.internalHorizontalLayout))

    def add_bot_group_box(self, horizontal_layout_widget, internal_horizontal_layout):
        a = AddBotLayout(horizontal_layout_widget, internal_horizontal_layout)
        self.bot_box_groups.append(a)

    def add_bot_group_box_click(self, horizontal_layout_widget, internal_horizontal_layout):
        self.add_bot_group_box(horizontal_layout_widget, internal_horizontal_layout)
        self.retranslate_ui_boxes(self._translate)

    def setup_db_status_frame(self):
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-9, 137, 101, 41))
        self.frame.setObjectName("frame")
        self.db_status_icon = QtWidgets.QLabel(self.frame)
        self.db_status_icon.setGeometry(QtCore.QRect(12, 18, 15, 15))
        self.db_status_icon.setText("")
        self.db_status_icon.setPixmap(QtGui.QPixmap("gui/icons/offline380x380.png"))
        self.db_status_icon.setScaledContents(True)
        self.db_status_icon.setObjectName("db_status_icon")
        self.db_status_label = QtWidgets.QLabel(self.frame)
        self.db_status_label.setEnabled(False)
        self.db_status_label.setGeometry(QtCore.QRect(22, 18, 47, 13))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.db_status_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.db_status_label.setFont(font)
        self.db_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_status_label.setObjectName("db_status_label")

    def setup_db_status_group(self):
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 430, 101, 41))
        self.groupBox.setObjectName("groupBox")
        self.db_status_icon = QtWidgets.QLabel(self.groupBox)
        self.db_status_icon.setGeometry(QtCore.QRect(12, 18, 15, 15))
        self.db_status_icon.setText("")
        self.db_status_icon.setPixmap(QtGui.QPixmap("gui/icons/offline380x380.png"))
        self.db_status_icon.setScaledContents(True)
        self.db_status_icon.setObjectName("db_status_icon")
        self.db_status_label = QtWidgets.QLabel(self.groupBox)
        self.db_status_label.setEnabled(False)
        self.db_status_label.setGeometry(QtCore.QRect(32, 18, 47, 13))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 131, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.db_status_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.db_status_label.setFont(font)
        self.db_status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.db_status_label.setObjectName("db_status_label")


    def connect_funcs_with_buttons(self):

        self.actionPrivet.triggered.connect(self.db_status_update_button)
        self.actionExit.triggered.connect(self.exit_app)

        self.actionContact_Baganec.triggered.connect(lambda: self.contact_baganec)
        self.actionContact_Germanec.triggered.connect(lambda: self.contact_germanec)
        self.actionAbout.triggered.connect(lambda: self.about)

    def contact_baganec(self):
        pass

    def contact_germanec(self):
        pass

    def about(self):
        pass

    def exit_app(self):
        pass

    def shefer1_click_event(self):
        self.controller.start_bot()

    def shefer2_click_event(self, argument):
        self.controller.stop_bot()

    def shefer3_click_event(self, argument1, argument2):
        self.controller.windows()

    def clicked(self, text):
        pass
        # self.label.setText(text)

    def db_status_update(self, is_available):
        if is_available:
            self.db_status_label.setEnabled(True)
            self.db_status_label.setText("Online")
            self.db_status_icon.setPixmap(QtGui.QPixmap("gui/icons/online380x380.png"))
        else:
            self.db_status_label.setEnabled(False)
            self.db_status_label.setText("Offline")
            self.db_status_icon.setPixmap(QtGui.QPixmap("gui/icons/offline380x380.png"))

    def db_status_update_button(self):
        self.controller.call_test_func(1)

    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle(self._translate("MainWindow", "EBVDAS software"))
        self.db_status_label.setText(self._translate("MainWindow", "Offline"))

        self.retranslate_ui_boxes(self._translate)

        self.menuFile.setTitle(self._translate("MainWindow", "File"))
        self.menuHelp.setTitle(self._translate("MainWindow", "Help"))
        self.menuFishers.setTitle(self._translate("MainWindow", "Create bot"))
        self.actionPrivet.setText(self._translate("MainWindow", "Privet😂"))
        self.actionPrivet.setStatusTip(self._translate("MainWindow", "Бесполезная кнопка"))
        self.action_5.setText(self._translate("MainWindow", "😂"))
        self.actionContact_Baganec.setText(self._translate("MainWindow", "Contact Baganec"))
        self.actionContact_Germanec.setText(self._translate("MainWindow", "Contact Germanec"))
        self.actionAbout.setText(self._translate("MainWindow", "About!"))
        self.actionAbout.setStatusTip(self._translate("MainWindow", "О двух физиках, которым было лень рыбачить "
                                                                    "самим..."))
        self.actionAbout.setShortcut(self._translate("MainWindow", "Ctrl+M"))
        self.actionExit.setText(self._translate("MainWindow", "Exit"))
        self.actionNew_fisher.setText(self._translate("MainWindow", "New fisher"))
        self.actionNew_fisher.setStatusTip(self._translate("MainWindow", "Создает нового бота для рыбалки"))
        self.actionNew_supplier.setText(self._translate("MainWindow", "New supplier"))
        self.actionNew_supplier.setStatusTip(self._translate("MainWindow", "Создает нового бота для раздачи ресурсов"))
        self.actionNew_farmer.setText(self._translate("MainWindow", "New farmer"))
        self.actionNew_farmer.setStatusTip(self._translate("MainWindow", "Создает нового бота для фарма"))
        self.actionNew_observer.setText(self._translate("MainWindow", "New observer"))
        self.actionNew_observer.setStatusTip(
            self._translate("MainWindow", "Создает нового бота для наблюдения за ценами у брокера"))

    def retranslate_ui_boxes(self, _translate):
        for b in self.bot_box_groups:
            b.botGroupBox.setTitle(_translate("MainWindow", "Bot"))
            b.startBotButton.setText(_translate("MainWindow", "Start"))
            b.stopBotButton.setText(_translate("MainWindow", "Stop"))
            b.isBroker.setText(_translate("MainWindow", "Broker"))
            b.isTrader.setText(_translate("MainWindow", "Trader"))
            b.accountsList.setItemText(0, _translate("MainWindow", "BaganskySilach"))
            b.accountsList.setItemText(1, _translate("MainWindow", "PortovayaShhuna"))

    def send_message(self, message):
        temp = 'View' + ': ' + message
        print(temp)


class AddBotLayout:
    def __init__(self, horizontal_layout_widget, internal_horizontal_layout):
        self.botGroupBox = QtWidgets.QGroupBox(horizontal_layout_widget)
        self.botGroupBox.setMinimumSize(QtCore.QSize(181, 151))
        self.botGroupBox.setMaximumSize(QtCore.QSize(181, 151))
        self.botGroupBox.setObjectName("botGroupBox")
        self.startBotButton = QtWidgets.QPushButton(self.botGroupBox)
        self.startBotButton.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.startBotButton.setFont(font)
        self.startBotButton.setObjectName("startBotButton")
        self.stopBotButton = QtWidgets.QPushButton(self.botGroupBox)
        self.stopBotButton.setGeometry(QtCore.QRect(100, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stopBotButton.setFont(font)
        self.stopBotButton.setObjectName("stopBotButton")
        self.botInfo = QtWidgets.QLabel(self.botGroupBox)
        self.botInfo.setGeometry(QtCore.QRect(70, 20, 101, 51))
        self.botInfo.setText("")
        self.botInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.botInfo.setObjectName("botInfo")
        self.isBroker = QtWidgets.QRadioButton(self.botGroupBox)
        self.isBroker.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.isBroker.setObjectName("isBroker")
        self.isTrader = QtWidgets.QRadioButton(self.botGroupBox)
        self.isTrader.setEnabled(False)
        self.isTrader.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.isTrader.setObjectName("isTrader")
        self.accountsList = QtWidgets.QComboBox(self.botGroupBox)
        self.accountsList.setGeometry(QtCore.QRect(10, 80, 161, 21))
        self.accountsList.setObjectName("accountsList")
        self.accountsList.addItem("")
        self.accountsList.addItem("")

        internal_horizontal_layout.addWidget(self.botGroupBox)


class ViewTest(WindowUI):
    def __init__(self, controller):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.controller = controller

        super(ViewTest, self).__init__(self.MainWindow, self.controller)
        self.MainWindow.show()
