from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys


def a():
    class App(QWidget):
        def __init__(self):
            super(App, self).__init__()
            self.start()

        def start(self):
            self.ui = uic.loadUi('instruction.ui')
            self.ui.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     a()
#     app.exec_()
