import sympy as sp
from sympy.utilities.lambdify import lambdify
from math import exp, log, ceil
x = sp.symbols('x')


eps = 0.0001
def newton_raphson(polynom, start, end):
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
    return [x_next, counter]

def bisection_method(polynom, start, end):
    f = lambdify(x, polynom)
    max_iterations = log(eps/(end-start), exp(1))
    max_iterations /= -log(2, exp(1))
    max_iterations = ceil(max_iterations)
    x_l = start
    x_r = end
    counter = 0
    x_c = (x_l + x_r) / 2
    while abs(x_r - x_l) > eps and f(x_c) != 0:
        counter += 1
        x_c = (x_l + x_r) / 2
        if(f(x_c) * f(x_r)) < 0:
            x_l = x_c
        else:
            x_r = x_c
        if counter > max_iterations:
            print("cannot resolve")
            return None
    return [x_c, counter]

def secant_method(polynom, start, end):
    f = lambdify(x, polynom)
    x_current = start
    x_prev = end
    counter = 0
    while abs(x_current - x_prev) > eps:
        counter += 1
        x_next = (x_prev*f(x_current) - x_current*f(x_prev)) / (f(x_current) - f(x_prev))
        x_prev = x_current
        x_current = x_next
    print(x_current)
    return [x_current, counter]
