from random import randint, choice
from sympy import solveset, Eq, Symbol
from operator import add, truediv, mul, sub

# 5*x=25 пример генерации


def do_generation_k():
    """
    Функция генериурет коэфициент и ответ уравения
    """
    k1 = randint(1, 100)
    answer = randint(1, 100)
    return k1, answer


def do_generate_char_eq():
    """
    Функция генерирует операцию
    """
    operation = ['+', '-', '*', '/']
    char = choice(operation)

    operation_dict = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    return operation_dict[char], char


def solution():
    """
    Функиця решает уравнения и возвращает ответ
    """
    char, user_char = do_generate_char_eq()
    k1, answer = do_generation_k()
    equation_user = f'{k1}{user_char}x={answer}'
    x = Symbol('x')
    return solveset(Eq(char(k1, x), answer), x), equation_user




