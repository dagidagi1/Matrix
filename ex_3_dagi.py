import sympy as sp
from math import log
from math import exp
from math import ceil
from sympy.utilities import lambdify
from sympy.utilities.lambdify import lambdify
x =sp.symbols('x')
my_f=x**3+2*x+5
#print("my_func: ",my_f)
#my_f1=sp.diff( my_f,x)
#print("f' : ",my_f1)
#f = lambdify(x,my_f1)
#print("f'(3): ",f(3))
#d1=sp.diff(my_f1)
#print("f'': ",d1)


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
    f_dif = sp.diff(polynom, x)
    f = lambdify(x, polynom)
    f_dif = lambdify(x, f_dif)
    x_l = start
    x_r = end
    #check maximum number of iterations depends on error size.
    max_iterations = log(eps / (end-start), exp(1))
    max_iterations /= -log(2, exp(1))
    max_iterations = ceil(max_iterations)
    counter = 0
    if (f(x_l) * f(x_r)) < 0:
        while (x_r - x_l > eps):
            counter += 1
            x_c = (x_l + x_r) / 2
            if(f(x_c) * f(x_r)) < 0:
                x_l = x_c
            else:
                x_r = x_c
            if (counter > max_iterations):
                print("cannot solve")
                return
    else:
        while (abs(x_r - x_l) > eps and f(x_c) !=0):
            counter += 1
            x_c = (x_l + x_r) / 2
            if (f_dif(x_c) * f_dif(x_r)) < 0:
                x_l = x_c
            else:
                x_r = x_c
            if(counter > max_iterations):
                print("cannot solve")
                return
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
f1 = x**4 +x**3-3*x**2
bisection_method(f1,-6,-1)
#newton_raphson(my_f,-8,0)