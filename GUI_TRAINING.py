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
        self.info_win_btn()
        self.ui_init_set()
        self.btn_check()
        self.lvl_choice()
        self.hide_dif()
        self.counter_try = 0
        self.answer = 0

    def start(self):  # start the app
        self.ui = uic.loadUi('train.ui')
        self.ui.show()

    def ui_init_set(self):  # settings window
        self.ui.answer.setPlaceholderText('Ответ')
        self.ui.counter.setText('0')
        self.ui.setFixedSize(1000, 700)
        self.ui.setWindowTitle('Doceo')

    def info_win_btn(self):  # scd window btn
        self.ui.pushButton_2.clicked.connect(lambda: self.show_info())

    def show_info(self):  # scd window with instruction
        self.ui_info = uic.loadUi('instruction.ui')
        self.ui_info.setFixedSize(800, 530)
        self.ui_info.show()

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

    def output_line_ez(self):  # set eq in lbl and check answer ez
        eq, self.x = l1.answer_ez()
        if self.int_answer(self.x):
            self.x = int(self.x)
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = str(self.x)
        # self.disable_btn()
        print(self.answer)
        self.ui.answer.setText('')

    def output_lien_avg(self):  # set eq in lbl and check answer avg
        eq, self.x = l2.answer_avg()
        print(self.x)
        if self.int_answer(self.x):
            self.x = int(self.x)
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = str(self.x)
        # self.disable_btn()
        self.ui.answer.setText('')

    def output_line_pro(self):  # set eq in lbl and check answer pro
        eq, self.x = l3.answer_hard()
        print(self.x)
        if self.int_answer(self.x):
            self.x = int(self.x)
        self.ui.eq_label.setText(f'{eq}\nx={self.x}')
        self.answer = str(self.x)
        #self.disable_btn()
        self.ui.answer.setText('')

    def btn_check(self):  # check answer btn
        self.ui.cheker.clicked.connect(lambda: self.check_event())

    def check_event(self):  # check answer
        value_ans = str(self.ui.answer.text())
        if self.answer != 0:
            if value_ans != self.answer:
                self.change_color()
                self.disable_btn()
                self.ui.corr.setText('Попробуй еще раз')
                self.counter_try = int(self.counter_try)
                self.counter_try += 1
                self.counter_try = str(self.counter_try)
                self.ui.counter.setText(self.counter_try)
            else:
                self.com_color()
                self.enable_bnt()
                self.ui.corr.setText('Молодец, все правильно')
                self.counter_try = 0
                self.ui.counter.setText('0')
                self.enable_bnt()

    @staticmethod
    def int_answer(n):
        if '.' in str(n) and len(str(n)[str(n).index('.'):]) == 2 \
                and str(n)[str(n).index('.') + 1] == '0':
            return True
        return False

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

    def change_color(self):
        self.ui.quadratic.setStyleSheet('background: 887CAF')
        self.ui.linear.setStyleSheet('background: 887CAF')
        self.ui.ez_line.setStyleSheet('background: 887CAF')
        self.ui.avg_line.setStyleSheet('background: 887CAF')
        self.ui.pushButton.setStyleSheet('background: 887CAF')

    def com_color(self):
        self.ui.quadratic.setStyleSheet('background: #16295')
        self.ui.linear.setStyleSheet('background: #16295')
        self.ui.ez_line.setStyleSheet('background: #16295')
        self.ui.avg_line.setStyleSheet('background: #16295')
        self.ui.pushButton.setStyleSheet('background: #16295')

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
