import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QGridLayout, QApplication

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addButton = QPushButton("add")
        #once click the addButton, call add() function
        self.addButton.clicked.connect(self.add)

        self.delButton = QPushButton("delete")
        self.delButton.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.addButton, 0, 0)
        self.layout.addWidget(self.delButton, 0, 1)

        self.setLayout(self.layout)

        self.setWindowTitle('add')
        self.show()

    def add(self):
        Button1 = QPushButton("1")
        self.layout.addWidget(Button1, 1, 0)

        Button2 = QPushButton("2")
        self.layout.addWidget(Button2, 1, 1)

    def delete(self):
        #the indexes of widgets we want to remove is 2 and 3
        self.layout.itemAt(2).widget().deleteLater()
        self.layout.itemAt(3).widget().deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())