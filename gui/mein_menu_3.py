# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu_3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-9, 137, 101, 41))
        self.frame.setObjectName("frame")
        self.db_status_icon = QtWidgets.QLabel(self.frame)
        self.db_status_icon.setGeometry(QtCore.QRect(12, 18, 15, 15))
        self.db_status_icon.setText("")
        self.db_status_icon.setPixmap(QtGui.QPixmap("../../../Tech/bs.png"))
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


        self.botGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
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
        self.internalHorizontalLayout.addWidget(self.botGroupBox)


        self.botGroupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.botGroupBox_2.setMinimumSize(QtCore.QSize(181, 151))
        self.botGroupBox_2.setMaximumSize(QtCore.QSize(181, 151))
        self.botGroupBox_2.setObjectName("botGroupBox_2")
        self.startBotButton_9 = QtWidgets.QPushButton(self.botGroupBox_2)
        self.startBotButton_9.setGeometry(QtCore.QRect(10, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.startBotButton_9.setFont(font)
        self.startBotButton_9.setObjectName("startBotButton_9")
        self.stopBotButton_9 = QtWidgets.QPushButton(self.botGroupBox_2)
        self.stopBotButton_9.setGeometry(QtCore.QRect(100, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.stopBotButton_9.setFont(font)
        self.stopBotButton_9.setObjectName("stopBotButton_9")
        self.botInfo_9 = QtWidgets.QLabel(self.botGroupBox_2)
        self.botInfo_9.setGeometry(QtCore.QRect(70, 20, 101, 51))
        self.botInfo_9.setText("")
        self.botInfo_9.setAlignment(QtCore.Qt.AlignCenter)
        self.botInfo_9.setObjectName("botInfo_9")
        self.isBroker_5 = QtWidgets.QRadioButton(self.botGroupBox_2)
        self.isBroker_5.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.isBroker_5.setObjectName("isBroker_5")
        self.isTrader_5 = QtWidgets.QRadioButton(self.botGroupBox_2)
        self.isTrader_5.setEnabled(False)
        self.isTrader_5.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.isTrader_5.setObjectName("isTrader_5")
        self.accountsList_5 = QtWidgets.QComboBox(self.botGroupBox_2)
        self.accountsList_5.setGeometry(QtCore.QRect(10, 80, 161, 21))
        self.accountsList_5.setObjectName("accountsList_5")
        self.accountsList_5.addItem("")
        self.accountsList_5.addItem("")
        self.internalHorizontalLayout.addWidget(self.botGroupBox_2)


        self.externalHorizontalLayout.addLayout(self.internalHorizontalLayout)


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
        icon.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBotButton.setIcon(icon)
        self.addBotButton.setIconSize(QtCore.QSize(75, 75))
        self.addBotButton.setObjectName("addBotButton")
        self.externalHorizontalLayout.addWidget(self.addBotButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.externalHorizontalLayout.addItem(spacerItem)

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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.db_status_label.setText(_translate("MainWindow", "Offline"))
        self.botGroupBox.setTitle(_translate("MainWindow", "Bot"))
        self.startBotButton.setText(_translate("MainWindow", "Start"))
        self.stopBotButton.setText(_translate("MainWindow", "Stop"))
        self.isBroker.setText(_translate("MainWindow", "Broker"))
        self.isTrader.setText(_translate("MainWindow", "Trader"))
        self.accountsList.setItemText(0, _translate("MainWindow", "BaganskySilach"))
        self.accountsList.setItemText(1, _translate("MainWindow", "PortovayaShhuna"))
        self.botGroupBox_2.setTitle(_translate("MainWindow", "Bot"))
        self.startBotButton_9.setText(_translate("MainWindow", "Start"))
        self.stopBotButton_9.setText(_translate("MainWindow", "Stop"))
        self.isBroker_5.setText(_translate("MainWindow", "Broker"))
        self.isTrader_5.setText(_translate("MainWindow", "Trader"))
        self.accountsList_5.setItemText(0, _translate("MainWindow", "BaganskySilach"))
        self.accountsList_5.setItemText(1, _translate("MainWindow", "PortovayaShhuna"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFishers.setTitle(_translate("MainWindow", "Create bot"))
        self.actionPrivet.setText(_translate("MainWindow", "Privet😂"))
        self.actionPrivet.setStatusTip(_translate("MainWindow", "Бесполезная кнопка"))
        self.action_5.setText(_translate("MainWindow", "😂"))
        self.actionContact_Baganec.setText(_translate("MainWindow", "Contact Baganec"))
        self.actionContact_Germanec.setText(_translate("MainWindow", "Contact Germanec"))
        self.actionAbout.setText(_translate("MainWindow", "About!"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "О двух физиках, которым было лень рыбачить самим..."))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_fisher.setText(_translate("MainWindow", "New fisher"))
        self.actionNew_fisher.setStatusTip(_translate("MainWindow", "Создает нового бота для рыбалки"))
        self.actionNew_supplier.setText(_translate("MainWindow", "New supplier"))
        self.actionNew_supplier.setStatusTip(_translate("MainWindow", "Создает нового бота для раздачи ресурсов"))
        self.actionNew_farmer.setText(_translate("MainWindow", "New farmer"))
        self.actionNew_farmer.setStatusTip(_translate("MainWindow", "Создает нового бота для фарма"))
        self.actionNew_observer.setText(_translate("MainWindow", "New observer"))
        self.actionNew_observer.setStatusTip(_translate("MainWindow", "Создает нового бота для наблюдения за ценами у брокера"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
