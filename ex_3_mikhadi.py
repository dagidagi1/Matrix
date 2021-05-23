import sympy as sp
import ex_3_dagi


def input_data():
    global polynomial, start, end, x
    deg = int(input("Which degree of function?: "))
    print("Enter function")
    for i in range(deg, -1, -1):
        t = float(input(f"(x**{i})*"))
        polynomial += t * x ** i
    start = float(input("Start point: "))
    end = float(input("End point: "))
    print(f"Your func: {polynomial}, Range[{start},{end}]")


def main():
    global polynomial, start, end, x
    print("""Choose preferred method:
    1 - Bisection method
    2 - Newton-Raphson method
    3 - Secant method""")
    choice = int(input())
    method = None
    if choice == 1:
        method = bisection_method
    elif choice == 2:
        method = ex_3_dagi.newton_raphson
    elif choice == 3:
        method = ex_3_dagi.secant_method
    else:
        print("Error")
    func = sp.lambdify(x, polynomial)
    p_dif = sp.diff(polynomial, x)
    f_dif = sp.lambdify(x, p_dif)
    solution = []
    while start < end:
        if func(start)*func(start + 0.1) < 0:
            temp = method(polynomial, start, (start + 0.1))
            if temp is not None:
                solution.append(temp)
        elif method == bisection_method:
            if f_dif(start)*f_dif(start+0.1) < 0:
                temp = method(p_dif, start, (start + 0.1))
                if temp is not None:
                    if func(temp[0]) == 0:
                        solution.append(temp)
        start += 0.1
    for i in solution:
        if i is not None:
            print(f"{i[0]}, found within {i[1]} attempts")


def bisection_method(polynom, start, end):
    func = sp.lambdify(x, polynom)
    x_l = start
    x_r = end
    counter = 0
    x_c = 1
    while abs(x_r - x_l) > eps:
        counter += 1
        x_c = (x_l + x_r) / 2
        if (func(x_l) * func(x_c)) > 0:
            x_l = x_c
        else:
            x_r = x_c
    return x_c, counter


x = sp.symbols('x')
eps = 0.0001
polynomial = 0
start = 0
end = 0
input_data()
main()
