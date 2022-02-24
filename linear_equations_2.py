from random import randint, choice
from tkinter.filedialog import askopenfiles
from sympy import solveset, Eq, Symbol
from operator import add, truediv, mul, sub
from fractions import Fraction

# 25*(x+4)=3 пример генерации


def numbers_dot(n):  # проверка кол-ва знаков после точки
    n = str(n)
    if '/' not in n:
        return True
    elif n == 'mptySe':
        return True
    else:
        z = n[1:n.index('/')]
        s = n[n.index('/') + 1:-1]
        o = int(z) / int(s)
        if '.' in str(o):
            if len(str(o)[str(o).index('.'):]) > 4:
                return False
            else:
                return True
        else:
            return True


def do_decimal(n):
    """
    Функция возвращает число в десятичной дроби
    """
    n = str(n)[1:-1]
    try:
        n = Fraction(n)
        num, dem = n.as_integer_ratio()
        return num / dem
    except ValueError:
        return '000'


def generation_kk():
    """
    Функция генериурет два коэфф и ответ
    """
    k1 = randint(1, 100)
    k2 = randint(1, 100)
    answer = randint(1, 100)
    return k1, k2, answer


def generate_chars_eq():
    """
    Функция генерирует две операции для уравнения
    """
    operation = ['+', '-', '/', '*']
    char1 = choice(operation)
    char2 = choice(operation)

    operation_dict = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return operation_dict[char1], operation_dict[char2], char1, char2


def solution():
    """
    Функция решает уравнение
    """
    char1, char2, user_char1, user_char2 = generate_chars_eq()
    k1, k2, answer = generation_kk()
    equation_user = f'{k1}{user_char1}({k2}{user_char2}x)={answer}'
    x = Symbol('x')
    root = solveset(Eq(char1(k1, char2(k2, x)), answer), x)
    return equation_user, root


def answer_avg():
    eq, r = solution()
    if not(numbers_dot(r)):
        return eq, r
    r = do_decimal(r)
    return eq, r
