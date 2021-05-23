import sympy as sp
from sympy.utilities import lambdify
from sympy.utilities.lambdify import lambdify
x =sp.symbols('x')


eps = 0.0001
def newton_raphson(polynom, start, end):
    x = sp.symbols('x')
    f = lambdify(x,polynom)
    f_dif = sp.diff(polynom,x)
    f_dif = lambdify(x,f_dif)
    counter = 0
    x_next = (start + end) / 2
    while(f(x_next) != 0):
        counter+=1
        print(counter)
        x_current = x_next
        x_next = x_current - f(x_current)/f_dif(x_current)
    return x_next, counter

def bisection_method(polynom, start, end):
    x = sp.symbols('x')
    f = lambdify(x, polynom)
    f_dif = sp.diff(polynom, x)
    f_dif = lambdify(x, f_dif)
    x_l = start
    x_r = end
    counter = 0
    x_c = 1
    if (f(x_l) * f(x_r)) < 0:
        while (x_r - x_l > eps):
            counter += 1
            x_c = (x_l + x_r) / 2
            if(f(x_c) * f(x_r)) < 0:
                x_l = x_c
            else:
                x_r = x_c
    else:
        while (abs(x_r - x_l) > eps):
            counter += 1
            x_c = (x_l + x_r) / 2
            if (f_dif(x_c) * f_dif(x_r)) < 0:
                x_l = x_c
            else:
                x_r = x_c
    print(x_c)
    return x_c, counter

def secant_method(polynom, start, end):
    x = sp.symbols('x')
    f = lambdify(x, polynom)
    x_current = start
    x_prev = end
    counter = 0
    while(abs(x_current - x_prev) > eps):
        counter += 1
        x_next = (x_prev*f(x_current) - x_current*f(x_prev)) / (f(x_current) - f(x_prev))
        x_prev = x_current
        x_current = x_next
    print(x_current)
    return x_current, counter
