import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox
from ui_hw7 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()
        self.menu = [self.cheeseburger, self.humburger, self.cocacola, self.naggets]

    def initui(self):
        self.cheeseburger.stateChanged.connect(self.clickBox1)
        self.humburger.stateChanged.connect(self.clickBox2)
        self.cocacola.stateChanged.connect(self.clickBox3)
        self.naggets.stateChanged.connect(self.clickBox4)
        self.pushButton.clicked.connect(self.order)

    def clickBox1(self, state):
        if state == QtCore.Qt.Checked:
            self.count_cheeseburger.setText("1")
        else:
            self.count_cheeseburger.setText("0")

    def clickBox2(self, state):
        if state == QtCore.Qt.Checked:
            self.count_humburger.setText("1")
        else:
            self.count_humburger.setText("0")

    def clickBox3(self, state):
        if state == QtCore.Qt.Checked:
            self.count_cocacola.setText("1")
        else:
            self.count_cocacola.setText("0")

    def clickBox4(self, state):
        if state == QtCore.Qt.Checked:
            self.count_naggets.setText("1")
        else:
            self.count_naggets.setText("0")

    def order(self):
        lst = ["Ваш заказ:", ' ']
        lst1 = []
        if self.cheeseburger.isChecked():
            lst1.append(self.count_cheeseburger.text())
            lst1.append("чизбургер")
            lst.append(f"чизбургер-----{lst1[0]}-----{int(lst1[0])*52}")

        lst2 = []
        if self.humburger.isChecked():
            lst2.append(self.count_humburger.text())
            lst2.append("гамбургер")
            lst.append(f"гамбургер-----{lst2[0]}-----{int(lst2[0]) * 49}")

        lst3 = []
        if self.cocacola.isChecked():
            lst3.append(self.count_cocacola.text())
            lst3.append("кока-кола")
            lst.append(f"кока-кола-----{lst3[0]}-----{int(lst3[0]) * 89}")

        lst4 = []
        if self.naggets.isChecked():
            lst4.append(self.count_naggets.text())
            lst4.append("наггетсы")
            lst.append(f"наггетсы-----{lst4[0]}-----{int(lst4[0]) * 189}")

        self.plainTextEdit.setPlainText('\n'.join(map(str, lst)))

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