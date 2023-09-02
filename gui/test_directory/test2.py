import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QWidget, QPushButton,
    QHBoxLayout, QGridLayout,
    QApplication,
    QMainWindow,
)


from gui.gui_resources import GUIResources


class MainWindow(QMainWindow):
    def __init__(self, gui_resources: GUIResources):
        super().__init__()

        self.setWindowTitle(gui_resources.window_name)
        icon = QIcon(gui_resources.icon_path)
        self.setWindowIcon(icon)


if __name__ == '__main__':
    # Нужен один и только один экземпляр QApplication
    # в конструктор можно передавать аргументы командной строки
    # (скорее всего, для нас это неактуально),
    # но если бы понадобилось, то это выглядело бы так:
    # app = QApplication(sys.argv)
    app = QApplication([])

    # создаём виджет
    window = MainWindow(GUIResources())
    window.show()  # окно по умолчанию скрыто!!!! Поэтому вызываем .show()

    # запускаем цикл событий
    # (https://habrastorage.org/r/w1560/getpro/habr/upload_files/919/88b/636/91988b6363fd2bf413509e133ea5b0c5.png)
    app.exec()

    # Приложение не доберётся сюда, пока не выйдем в очко и цикл
    # событий не остановится.
