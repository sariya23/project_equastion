from random import randint


def quadratic():
    x1 = randint(1, 100)
    x2 = randint(1, 100)
    a = 1
    b = (x1 + x2)*(-1)
    c = x1*x2
    if b > 0:
        b_user = f'+{b}'
    else:
        b_user = f'{b}'
    if c > 0:
        c_user = f'+{c}'
    else:
        c_user = f'{c}'
    D = b**2 - 4*a*c
    equation_user = f'x²{b_user}x{c_user}=0'
    return equation_user, D, x1, x2
