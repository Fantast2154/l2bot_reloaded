import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import uic


class GUITestHandler:
    def __init__(self):
        pass

    def eat(self):
        print('Ем тебя.')


class MySecondWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_test02.ui", self)


class MyWidget(QWidget):
    def __init__(self, handler):
        super().__init__()
        uic.loadUi("ui_test01.ui", self)
        #self.w = uic.loadUi("ui_test02.ui", self)
        # uic.loadUi("ui_test01.ui", self)

        # либо через хендлер
        # self.connect_buttons_to_handler(handler)

        # либо прямо в текущем классе цепляемся
        self.connect_buttons_to_this_class_methods()

    def connect_buttons_to_handler(self, handler):
        self.eat_me_button.clicked.connect(lambda: handler.eat())

    def connect_buttons_to_this_class_methods(self):
        self.eat_me_button.clicked.connect(lambda: self.on_eat_me_event())

    def on_eat_me_event(self):
        self.eat_me_label.setText("Ем тебz.")
        #print(self.myhorizontalLayout.__dir__())
        #print(self.w.__dir__())
        # print(self.myhorizontalLayout.addWidget(QPushButton("qwe")))
        w = MySecondWidget()
        print(w)
        print(self.myhorizontalLayout.addWidget(w))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    handler = GUITestHandler()
    ex = MyWidget(handler)
    ex.show()
    sys.exit(app.exec_())
