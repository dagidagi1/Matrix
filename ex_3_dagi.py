import sympy as sp
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
    f = lambdify(x, polynom)
    x_l = start
    x_r = end
    counter = 0
    while(x_r - x_l > eps):
        counter += 1
        x_c = (x_l + x_r) / 2
        if(f(x_c) * f(x_r)) < 0:
            x_l = x_c
        else:
            x_r = x_c
    return x_c, counter

bisection_method(my_f,-8,1)
#newton_raphson(my_f,-8,0)