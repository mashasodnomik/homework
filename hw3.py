import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_hw_3 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()


    def initui(self):
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_minus.clicked.connect(self.minus)
        self.pushButton_mltpl.clicked.connect(self.mltp)

    def plus(self):
        self.lineEdit_3.setText(str(int(self.lineEdit_1.text())+ int(self.lineEdit_2.text())))


    def minus(self):
        self.lineEdit_3.setText(str(int(self.lineEdit_1.text()) - int(self.lineEdit_2.text())))


    def mltp(self):
        self.lineEdit_3.setText(str(int(self.lineEdit_1.text()) * int(self.lineEdit_2.text())))

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













