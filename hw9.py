import sys
import random
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from ui_hw9 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.pushButton.clicked.connect(self.random)

    def random(self):
        lst = []
        with open("input.txt", "r") as f:
            for line in f:
                lst.append(line)
        self.lineEdit.setText(lst[int(random.randint(1, len(lst)))])

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())