import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import os

import quadranic as q
import linear_equations_1 as l1


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.start()
        self.choice()
        self.ui_init()
        self.btn_check()
        self.answer = 0
        self.flag = 0

    def start(self):  # start the app
        self.ui = uic.loadUi('train.ui')
        self.ui.show()

    def ui_init(self):  # answer space
        self.ui.answer.setPlaceholderText('Ответ')

    def choice(self):  # choice btn's
        self.ui.quadratic.clicked.connect(lambda: self.output_qua())
        self.ui.linear.clicked.connect(lambda: self.output_line())

    def output_qua(self):  # output eq
        eq, self.d, self.x1, self.x2 = q.quadratic()
        self.ui.label.setText(f'{eq}\nD={self.d}\nx1={self.x1}\nx2={self.x2}')
        self.answer = str(self.x1 + self.x2)
        self.flag = 1
        print(self.answer)

    def output_line(self):  # output eq
        self.x, eq = l1.solution()
        self.x = str(self.x)[1:-1]
        self.ui.label.setText(f'{eq}\nx={self.x}')
        self.answer = self.x
        print(self.answer)
        self.flag = 2

    def check_event(self):  # check answer
        value_ans = str(self.ui.answer.text())
        print(type(value_ans))
        if self.answer != 0:
            if value_ans != self.answer:
                self.ui.label_2.setText('Uncorrect')
                self.ui.quadratic.setEnabled(False)
                self.ui.linear.setEnabled(False)
            else:
                self.ui.label_2.setText('Correct')
                self.ui.quadratic.setEnabled(True)
                self.ui.linear.setEnabled(True)

    def btn_check(self):
        self.ui.pushButton.clicked.connect(lambda: self.check_event())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
