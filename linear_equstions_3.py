from random import randint, choice
from sympy import solveset, Eq, Symbol
from operator import add, truediv, mul, sub

from linear_equations_2 import numbers_dot, do_decimal
# 5*(x + 3) = 3(3 - x)


def generation_kkk():
    """
    Функция генерирует коэфф
    """
    k1 = randint(1, 100)
    k2 = randint(1, 100)
    k3 = randint(1, 100)
    k4 = randint(1, 100)
    return k1, k2, k3, k4


def generate_chars_eq():
    """
    Функция генерирует две операции для уравнения
    """
    operation = ['+', '-']
    char1 = choice(operation)
    char2 = choice(operation)
    operation_dict = {
        '+': add,
        '-': sub,
    }
    return operation_dict[char1], operation_dict[char2], char1, char2


def solution():
    """
    Функция решает уравнение
    """
    char1, char2, user_char1, user_char2 = generate_chars_eq()
    k1, k2, k3, k4 = generation_kkk()
    equation_user = f'{k1}*({k2}{user_char1}x)={k3}*({k4}{user_char2}x)'
    x = Symbol('x')
    root = solveset(Eq(mul(k1, char1(k2, x)), mul(k3, char2(k4, x))))
    return equation_user, root


def answer_hard():
    eq, r = solution()
    while not(numbers_dot(r)):
        eq, r = solution()
    r = do_decimal(r)
    return eq, r


