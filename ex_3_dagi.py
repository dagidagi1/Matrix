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
    f_dif = polynom.sp.diff(polynom,x)
    f_dif = lambdify(x,f_dif)
    counter = 0
    while(f(x_next) != 0):
        counter+=1
        print(counter)
        x_current = (start + end) / 2
        x_next = x_current - f(x_current)/f_dif(x_current)
    print(x_next)


newton_raphson(my_f,-2,0)