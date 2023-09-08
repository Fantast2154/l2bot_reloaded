import ctypes
import os
import warnings

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QWidget, QPushButton,
    QGridLayout,
    QApplication,
    QMainWindow, QTabWidget, QLabel, QMenuBar, QMenu,
    QAction, QHBoxLayout, QComboBox, QSpinBox, )

from gui.gui_resources import GUIResources, GUISettings
from PyQt5 import uic

from mathematics.vectors import Vector2i
from user_props.personal_settings import PersonalSettings


# from view_props.view import GUIHandler


class DeveloperWidget(QWidget):
    def __init__(self):
        super().__init__()
        # uic.loadUi('test_widget.ui', self)
        project_root = os.path.dirname(os.path.dirname(__file__))
        uic.loadUi(project_root + '/gui/developer_tab.ui', self)
        # uic.loadUi('test_folder/ui_test01.ui', self)


class MainWindow(QMainWindow):
    def __init__(self, gui_resources: GUIResources, gui_handler):
        super().__init__()
        self.developer_tab = None
        self.gui_resources = gui_resources
        self.gui_handler = gui_handler

        project_root = os.path.dirname(os.path.dirname(__file__))
        uic.loadUi(project_root + '/gui/main_window.ui', self)

        self.setup_ui()
        self.initialize_icons()
        self.initialize_characters_list()
        self.load_settings()

    def setup_ui(self):
        self.developer_tab = DeveloperWidget()
        self.my_horizontal_layout.addWidget(self.developer_tab, alignment=Qt.AlignVCenter | Qt.AlignHCenter)
        self.hook_to_all_buttons(self.developer_tab)

    def initialize_icons(self):
        self.internet_connection_update(False)

        self.setWindowIcon(QIcon(self.gui_resources.header_icon_path))
        self.setWindowTitle(self.gui_resources.window_name)

        self.save_position.setIcon(QIcon(self.gui_resources.save_icon_path))

        icons = [self.gui_resources.internet_connection_disabled_icon_path,
                 self.gui_resources.internet_connection_enabled_icon_path,
                 ]

        for i in range(0, self.tab_widget.count()):
            self.tab_widget.setTabIcon(i, QIcon(icons[i]))

    def initialize_characters_list(self):
        self.developer_tab.characters.addItems(PersonalSettings.names)
        self.developer_tab.characters.setCurrentText(PersonalSettings.names[0])

    def hook_to_all_buttons(self, widget):
        buttons = [name.lstrip('button_') for name in self.__dir__() if name.startswith('button_')]
        for b in buttons:
            button_method = self.__getattribute__('button_' + b)
            # widget.__dict__[b].clicked.connect(button_method)
            widget.__dict__[b].clicked.connect(lambda _, f=button_method: f())
            print(button_method)

        self.save_position.clicked.connect(lambda: self.save_settings())

    # TODO: clicked.connect В ЦИКЛЕ НЕ РАБОТАЕТ С ЛЯМБДАМИ!!!! ПОЧЕМУ? РАЗБОРАТЬСЯ! ЦЕПЛЯЕМСЯ БЕЗ ЛЯМБДЫ
    # UPDATE: https://stackoverflow.com/questions/3431676/creating-functions-or-lambdas-in-a-loop-or-comprehension
    # РЕШЕНИЕ: вместо .clicked.connect(lambda : button_method()) использовать
    # .clicked.connect(lambda _, f=button_method: f())
    # _ (нижнее подчеркивание) нужно, чтобы исбоавиться от БУЛЕВА значения в методе connect
    # https://stackoverflow.com/questions/18836291/lambda-function-returning-false
    '''
    #widget.__dict__[s[1]].clicked.connect(lambda: print(s[1]))
        # for b in buttons:
        #     button_method = self.__getattribute__('button_' + b)
        #     #widget.__dict__[b].clicked.connect(lambda: print(b,' ---- ', button_method)) 

        #     print(b)
        #     f = widget.__dict__[b]
        #     f.clicked.connect(lambda: print(f))
        #     print(f)
        #     counter += 1
    '''

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        super().moveEvent(event)
        self.save_position.setEnabled(True)

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
        self.save_position.setEnabled(False)

    def set_settings(self, settings: GUISettings):
        x = settings.position.x
        y = settings.position.y
        self.move(x, y)

    def set_default_settings(self):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        width = self.width()
        height = self.height()

        left_top_x = screensize[0] - 2 * width
        left_top_y = screensize[1] - height - 50
        self.move(left_top_x, left_top_y)

    def internet_connection_update(self, connected):
        if connected:
            self.internet_connection_label.setEnabled(True)
            self.internet_connection_label.setText("Online")
            self.internet_connection_icon.setPixmap(
                QtGui.QPixmap(self.gui_resources.internet_connection_enabled_icon_path))
        else:
            self.internet_connection_label.setEnabled(False)
            self.internet_connection_label.setText("Offline")
            self.internet_connection_icon.setPixmap(
                QtGui.QPixmap(self.gui_resources.internet_connection_disabled_icon_path))

    def button_launch_windows(self):
        value = self.developer_tab.windows_number.value()
        self.gui_handler.launch_windows(value)

    def button_relaunch_all_windows(self):
        self.gui_handler.relaunch_windows()

    def button_close_all_windows(self):
        self.gui_handler.close_all_windows()

    def button_relog_all_windows(self):
        self.gui_handler.relog_all_windows()

    def button_start_farm(self):
        self.gui_handler.start_bot()

    def button_stop_farm(self):
        self.gui_handler.stop_bot()

    def button_connect_to_server(self):
        self.gui_handler.connect_to_server()

    def button_run_server(self):
        self.gui_handler.run_server()

    def button_launch_login_from_list(self):
        self.gui_handler.launch_and_login_char(self.developer_tab.characters.currentText())

    def button_default_observing(self):
        self.gui_handler.login_default()

    def button_start_observing(self):
        print('start observing')

    def button_stop_observing(self):
        print('stop observing')


if __name__ == '__main__':
    # Нужен один и только один экземпляр QApplication
    # в конструктор можно передавать аргументы командной строки
    # (скорее всего, для нас это неактуально),
    # но если бы понадобилось, то это выглядело бы так:
    # app = QApplication(sys.argv)
    app = QApplication([])

    # создаём виджет
    resources = GUIResources()
    # handler = GUIHandler(None)

    window = MainWindow(resources, None)
    window.show()  # окно по умолчанию скрыто!!!! Поэтому вызываем .show()

    # запускаем цикл событий
    # (https://habrastorage.org/r/w1560/getpro/habr/upload_files/919/88b/636/91988b6363fd2bf413509e133ea5b0c5.png)
    app.exec()

    # Приложение не доберётся сюда, пока не выйдем в очко и цикл
    # событий не остановится.
