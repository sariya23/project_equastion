from random import randint, choice
from sympy import solveset, Eq, Symbol
from operator import add, truediv, mul, sub
from fractions import Fraction

# 25*(x+4)=3 пример генерации


def numbers_dot(n):  # проверка кол-ва знаков после точки
    n = str(n)
    z = n[1:n.index('/')]
    s = n[n.index('/') + 1:-1]
    o = int(z) / int(s)
    if '.' in str(o):
        if len(str(o)[str(o).index('.'):]) > 3:
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
    n = Fraction(n)
    num, dem = n.as_integer_ratio()
    return num / dem


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
    return root, equation_user





################################

# counter = 1
# entry = 11


# while counter != entry:
#     root, eq = solution()
#     if '/' in str(root) and numbers_dot(root) == False:
#         continue
#     elif '/' in str(root) and numbers_dot(root):
#         root = do_decimal(root)
#     else:
#         root = str(root)[1:-1]
#     print(f'{counter}. {eq}')
#     print('Ответ: ', root)
#     print()
#     counter += 1

