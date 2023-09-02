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
from view.developer_widget import DebugWidget
from view.gui_handler import GuiHandler
from view.release_widget import ReleaseWidget


class MainWindow(QMainWindow):
    def __init__(self, gui_resources: GUIResources, gui_handler: GuiHandler):
        super().__init__()

        self.gui_resources = gui_resources
        self.gui_handler = gui_handler

        self.load_settings()
        self.setup_ui()

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        super().moveEvent(event)
        self.save_settings_button.setEnabled(True)

    def load_settings(self):
        try:
            self.set_settings(self.gui_resources.load_settings())
        except:
            warnings.formatwarning = lambda message, category, filename, lineno, file=None, line=None: \
                '%s:%s: %s: %s\n' % (filename, lineno, category.__name__, message)
            warnings.warn(f'No gui_settings file! Applying default settings...')
            self.set_default_settings()

    def save_settings(self):
        new_settings = GUISettings()

        position = self.pos()
        size = self.size()

        new_settings.position = Vector2i(position.x(), position.y())
        new_settings.size = Vector2i(size.width(), size.height())

        self.gui_resources.save_settings(new_settings)
        self.save_settings_button.setEnabled(False)

    def set_settings(self, settings: GUISettings):
        x = settings.position.x
        y = settings.position.y
        self.move(x, y)

        size = settings.size
        self.resize(size.x, size.y)
        self.setMinimumSize(QtCore.QSize(size.x, size.y))
        self.setMaximumSize(QtCore.QSize(size.x, size.y))

    def set_default_settings(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        width = 720
        height = 300

        left_top_x = screensize[0] - 2 * width
        left_top_y = screensize[1] - height - 50

        self.resize(width, height)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))
        self.move(left_top_x, left_top_y)

    def setup_ui(self):
        self.setWindowTitle(self.gui_resources.window_name)
        window_icon = QIcon(self.gui_resources.header_icon_path)
        self.setIconSize(QtCore.QSize(5, 5))
        self.setWindowIcon(window_icon)

        layout = QGridLayout()
        debug_widget = DebugWidget(self.gui_resources, self.gui_handler)
        release_widget = ReleaseWidget(self.gui_resources, self.gui_handler)

        self.save_settings_button = QPushButton()
        self.save_settings_button.setFlat(True)
        self.save_settings_button.setFixedSize(20, 20)
        self.save_settings_button.setIcon(QtGui.QIcon(self.gui_resources.save_icon_path))
        self.save_settings_button.setIconSize(QtCore.QSize(20, 20))
        self.save_settings_button.setToolTip('Save current position of gui window')
        self.save_settings_button.clicked.connect(lambda: self.save_settings())
        layout.addWidget(self.save_settings_button, 1, 0, alignment=Qt.AlignRight)

        self.setup_internet_icon(layout)
        # self.setup_window_menu()
        tab_widget = QTabWidget()
        tab_widget.addTab(debug_widget, 'Developer-tab')
        tab_widget.addTab(release_widget, 'Release-tab')
        layout.addWidget(tab_widget, 0, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def setup_internet_icon(self, layout):
        internetIcon = QLabel()
        internetIcon.setFixedSize(20, 20)
        internetIcon.setText("")
        internetIcon.setPixmap(QtGui.QPixmap(self.gui_resources.internet_connection_disabled_icon_path))
        internetIcon.setScaledContents(True)
        internetIcon.setToolTip('Database status')
        layout.addWidget(internetIcon, 1, 0, alignment=Qt.AlignLeft)

        internet_connection_label = QLabel()
        internet_connection_label.setEnabled(False)
        internet_connection_label.setText("Offline")
        internet_connection_label.setToolTip('Database status')

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        #font.setWeight(500)

        internet_connection_label.setFont(font)
        internet_connection_label.setContentsMargins(20, 0, 0, 0)
        layout.addWidget(internet_connection_label, 1, 0, alignment=Qt.AlignLeft)

    def setup_window_menu(self):
        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setTitle("File")

        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setTitle("Help")

        self.menuFishers = QMenu(self.menubar)
        self.menuFishers.setTitle("Create bot")

        self.setMenuBar(self.menubar)

        self.actionPrivet = QAction(self)
        self.actionPrivet.setText("Privet😂")
        self.actionPrivet.setStatusTip("Бесполезная кнопка")

        self.action_5 = QAction(self)
        self.action_5.setText("😂")

        self.actionContact_Baganec = QAction(self)
        self.actionContact_Baganec.setText("Contact Baganec!!!")

        self.actionContact_Germanec = QAction(self)
        self.actionContact_Germanec.setText("Contact Germanec!!!")

        self.actionAbout = QAction(self)
        self.actionAbout.setText("About!")
        self.actionAbout.setStatusTip("О двух физиках, которым было лень рыбачить самим...")
        self.actionAbout.setShortcut("Ctrl+M")

        self.actionExit = QAction(self)
        self.actionExit.setText("Exit")

        self.actionNew_fisher = QAction(self)
        self.actionNew_fisher.setEnabled(False)
        self.actionNew_fisher.setText("New fisher")
        self.actionNew_fisher.setStatusTip("Создает нового бота для рыбалки")

        self.actionNew_supplier = QAction(self)
        self.actionNew_supplier.setEnabled(False)
        self.actionNew_supplier.setText("New supplier")
        self.actionNew_supplier.setStatusTip("Создает нового бота для раздачи ресурсов")

        self.actionNew_farmer = QAction(self)
        self.actionNew_farmer.setEnabled(False)
        self.actionNew_farmer.setText("New farmer")
        self.actionNew_farmer.setStatusTip("Создает нового бота для фарма")

        self.actionNew_observer = QAction(self)
        self.actionNew_observer.setEnabled(False)
        self.actionNew_observer.setText("New observer")
        self.actionNew_observer.setStatusTip("Создает нового бота для наблюдения за ценами у брокера")

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

    def contact_baganec(self):
        print('''
              Не беспокойтесь, пред Баганским Владыкой сего мира, времени и всего бытия, как и у ваших предков, 
              братьев и сестер, ваша жизнь не более ничтожна, чем жизнь любого живого существа на этой планете и 
              очень скоро ты убедишься в этом сам. Единственный скоро посетит вашу плоскость бытия, вот только ты 
              будешь не слишком то этому рад.
              ''')

    def contact_germanec(self):
        pass

    def about(self):
        print('''
              Бот без нормального ГУИ, базы данных, с кривонаписанным классами.. отрефакторить бы всё, 
              написать нормально сетевую часть И НА хотспрингс отправить. И ОН СТАНЕТ БОТОМ. ПРИ ЧЕМ БОТОМ БУДЕТ 
              АХУЕННЫМ. ПРАВИЛЬНО?
              ''')

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
        print('''
        — Давай базу данных.
        ...ты ебанулся? Какая база? Она померла уже 8 раз. И на поминках плясали, сука
        ''')
        # self.controller.call_test_func(1)

    def exit_app(self):
        pass


if __name__ == '__main__':
    # Нужен один и только один экземпляр QApplication
    # в конструктор можно передавать аргументы командной строки
    # (скорее всего, для нас это неактуально),
    # но если бы понадобилось, то это выглядело бы так:
    # app = QApplication(sys.argv)
    app = QApplication([])

    # создаём виджет
    window = MainWindow(GUIResources(), GuiHandler(None))
    window.show()  # окно по умолчанию скрыто!!!! Поэтому вызываем .show()

    # запускаем цикл событий
    # (https://habrastorage.org/r/w1560/getpro/habr/upload_files/919/88b/636/91988b6363fd2bf413509e133ea5b0c5.png)
    app.exec()

    # Приложение не доберётся сюда, пока не выйдем в очко и цикл
    # событий не остановится.
