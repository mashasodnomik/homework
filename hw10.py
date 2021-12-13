import sys
import os.path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from ui_hw10 import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.pushButton.clicked.connect(self.statistic)

    def statistic(self):
        if os.path.isfile(r"C:\Users\USER\PycharmProjects\homework_pyqt\%s." % self.lineEdit.text()) is False:
            self.label_5.setText(f"файла {self.lineEdit.text()} не существует")
        else:
            with open(self.lineEdit.text(), 'r') as f:
                lst = [int(x) for x in f.read().split(sep=None)]
                self.lineEdit_2.setText(str(max(lst)))
                self.lineEdit_3.setText(str(min(lst)))
                self.lineEdit_4.setText(str(sum(lst) / len(lst)))
                with open("output.txt", "w") as f:
                    f.write(f"max value: {max(lst)}, min value: {min(lst)}, average value: {sum(lst) / len(lst)} ")

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