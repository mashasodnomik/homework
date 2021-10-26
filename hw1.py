import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_hw1 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.pushButton.clicked.connect(self.magic)

    def magic(self):
        if self.pushButton.text() == "->":
            self.lineEdit.setText(" ")
            self.lineEdit_2.setText("Фокус")
            self.pushButton.setText("<-")
        else:
            self.lineEdit_2.setText(" ")
            self.lineEdit.setText("Фокус")
            self.pushButton.setText("->")


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

