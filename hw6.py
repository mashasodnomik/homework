import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_hw6 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()
        self.menu = [self.cheeseburger, self.humburger, self.cocacola, self.naggets]


    def initui(self):
        self.pushButton.clicked.connect(self.order)

    def order(self):
        lst = []
        if self.cheeseburger.isChecked():
            lst.append("чизбургер")

        if self.humburger.isChecked():
            lst.append("гамбургер")

        if self.cocacola.isChecked():
            lst.append("кокакола")

        if self.naggets.isChecked():
            lst.append("наггетсы")


        self.plainTextEdit.setPlainText(f'Ваш заказ: {" ".join(lst)}')









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