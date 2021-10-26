import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from ui_hw2 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initui()

    def initui(self):
        boxes = [(self.checkBox, self.label), (self.checkBox_2, self.label_2), (self.checkBox_3, self.label_3),
                 (self.checkBox_4, self.label_4)]
        for box in boxes:
            if box[0].isChecked() is False:
                box[0].stateChanged.connect(self.hide_label)


    def hide_label(self):
        boxes = [(self.checkBox, self.label), (self.checkBox_2, self.label_2), (self.checkBox_3, self.label_3),
                 (self.checkBox_4, self.label_4)]
        for box in boxes:
            if box[0].isChecked():
                box[1].hide()
            else:
                box[1].show()



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










