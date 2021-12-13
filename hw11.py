import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from ui_hw11 import Ui_MainWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        self.pushButton.clicked.connect(self.upl)

    def upl(self):
        with open("pushkin.txt", "r") as f:
            lst = [x for x in f.read().split("\n")]
            lst1 = []
            for i in range(0,len(lst), 2):
                lst1.append(lst[i])

            for i in range(1, len(lst)-1, 2):
                lst1.append(lst[i])
            print(lst1)
        self.plainTextEdit.setPlainText('/n'.join(lst1))

        sys.excepthook = sys.excepthook

        def exception_hook(exctype, value, traceback):
            sys._excepthook(exctype, value, traceback)
            sys.exit(1)

        sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())


