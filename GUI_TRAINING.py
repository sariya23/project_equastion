from random import randint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

import sys
import os
import quadranic as q
import linear_equations_1 as l1
import linear_equations_2 as l2
import linear_equstions_3 as l3


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.start()
        self.choice()
        self.ui_init()
        self.btn_check()
        self.lvl_choice()
        self.hide_dif()
        self.counter_try = 0
        self.answer = 0

    def start(self):  # start the app
        self.ui = uic.loadUi('train.ui')
        self.ui.show()

    def ui_init(self):  # answer space
        self.ui.answer.setPlaceholderText('Ответ')
        self.ui.counter.setText('0')

    def choice(self):  # choice btn's
        self.ui.quadratic.clicked.connect(lambda: self.output_qua())
        self.ui.linear.clicked.connect(lambda: self.show_dif())

    def lvl_choice(self):  # choice lvl
        self.ui.ez_line.clicked.connect(lambda: self.output_line_ez())
        self.ui.avg_line.clicked.connect(lambda: self.output_lien_avg())
        self.ui.pushButton.clicked.connect(lambda: self.output_line_pro())

    def output_qua(self):  # output eq
        eq, self.d, self.x1, self.x2 = q.quadratic()
        self.ui.eq_label.setText(
            f'{eq}\nD={self.d}\nx1={self.x1}\nx2={self.x2}')
        self.answer = str(self.x1 + self.x2)
        self.disable_btn()
        print(self.answer)
        self.ui.answer.setText('')

    def output_line_ez(self):  # output eq
        eq, self.x = l1.answer_ez()
        if '.' in str(self.x) and len(str(self.x)[str(self.x).index('.'):]) == 2 \
                and str(self.x)[str(self.x).index('.') + 1] == '0':
            self.x = int(self.x)
        elif '{' in str(self.x):  # if answer with '/'
            self.x = str(self.x)[1:-1]
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = self.x
        # self.disable_btn()
        print(self.answer)
        self.ui.answer.setText('')

    def output_lien_avg(self):  # method set the eq on label and treatmeant answer
        eq, self.x = l2.answer_avg()
        print(self.x)
        if '.' in str(self.x) and len(str(self.x)[str(self.x).index('.'):]) == 2\
                and str(self.x)[str(self.x).index('.') + 1] == '0':  # if answer int win dot 0
            self.x = int(self.x)
        elif '{' in str(self.x):  # if answer with '/'
            self.x = str(self.x)[1:-1]
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = str(self.x)
        # self.disable_btn()
        self.ui.answer.setText('')

    def output_line_pro(self):
        eq, self.x = l3.answer_hard()
        print(self.x)
        if '.' in str(self.x) and len(str(self.x)[str(self.x).index('.'):]) == 2\
                and str(self.x)[str(self.x).index('.') + 1] == '0':
            self.x = int(self.x)
        elif '{' in str(self.x):  # if answer with '/'
            self.x = str(self.x)[1:-1]
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = str(self.x)
        self.disable_btn()
        self.ui.answer.setText('')

    def btn_check(self):  # check answer btn
        self.ui.cheker.clicked.connect(lambda: self.check_event())

    def check_event(self):  # check answer
        value_ans = str(self.ui.answer.text())
        if self.answer != 0:
            if value_ans != self.answer:
                self.ui.result.setText('Uncorrect')
                self.disable_btn()
                self.counter_try = int(self.counter_try)
                self.counter_try += 1
                self.counter_try = str(self.counter_try)
                self.ui.counter.setText(self.counter_try)
            else:
                self.enable_bnt()
                self.counter_try = 0
                self.ui.counter.setText('0')
                self.ui.result.setText('Correct')
                self.enable_bnt()

    def disable_btn(self):  # block btn
        self.ui.quadratic.setEnabled(False)
        self.ui.linear.setEnabled(False)
        self.ui.ez_line.setEnabled(False)
        self.ui.avg_line.setEnabled(False)
        self.ui.pushButton.setEnabled(False)

    def enable_bnt(self):  # unblock btn
        self.ui.quadratic.setEnabled(True)
        self.ui.linear.setEnabled(True)
        self.ui.ez_line.setEnabled(True)
        self.ui.avg_line.setEnabled(True)
        self.ui.pushButton.setEnabled(True)

    def hide_dif(self):  # hide lvl of linear eq
        self.ui.ez_line.hide()
        self.ui.avg_line.hide()
        self.ui.pushButton.hide()

    def show_dif(self):  # show lvl of linear eq
        self.ui.ez_line.show()
        self.ui.avg_line.show()
        self.ui.pushButton.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
