import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from ui_hw4 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()
        self.txt = ''

    def initui(self):
        d = {
            self.pushButton_A: '.-',
            self.pushButton_B: '-...',
            self.pushButton_C: '-.-.',
            self.pushButton_D: '-..',
            self.pushButton_E: '.',
            self.pushButton_F: '..-.',
            self.pushButton_G: '--.',
            self.pushButton_H: '....',
            self.pushButton_I: '..',
            self.pushButton_J: '.---',
            self.pushButton_K: '-.-',
            self.pushButton_L: '.-..',
            self.pushButton_M: '--',
            self.pushButton_N: '-.',
            self.pushButton_O: '---',
            self.pushButton_P: '.--.',
            self.pushButton_Q: '--.-',
            self.pushButton_R: '.-.',
            self.pushButton_S: '...',
            self.pushButton_T: '-',
            self.pushButton_U: '..-',
            self.pushButton_V: '...-',
            self.pushButton_W: '.--',
            self.pushButton_X: '-..-',
            self.pushButton_Y: '-.--',
            self.pushButton_Z: '--..'

        }
        buttons = list(d.keys())

        for button in buttons:
            button.clicked.connect(self.vvod)
            button.setChecked(True)


    def vvod(self):
        d = {
            self.pushButton_A: '.-',
            self.pushButton_B: '-...',
            self.pushButton_C: '-.-.',
            self.pushButton_D: '-..',
            self.pushButton_E: '.',
            self.pushButton_F: '..-.',
            self.pushButton_G: '--.',
            self.pushButton_H: '....',
            self.pushButton_I: '..',
            self.pushButton_J: '.---',
            self.pushButton_K: '-.-',
            self.pushButton_L: '.-..',
            self.pushButton_M: '--',
            self.pushButton_N: '-.',
            self.pushButton_O: '---',
            self.pushButton_P: '.--.',
            self.pushButton_Q: '--.-',
            self.pushButton_R: '.-.',
            self.pushButton_S: '...',
            self.pushButton_T: '-',
            self.pushButton_U: '..-',
            self.pushButton_V: '...-',
            self.pushButton_W: '.--',
            self.pushButton_X: '-..-',
            self.pushButton_Y: '-.--',
            self.pushButton_Z: '--..'

        }

        self.txt += str(d[self.sender()])
        self.lineEdit.setText(self.txt)



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




