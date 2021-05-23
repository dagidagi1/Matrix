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
        method = ex_3_dagi.bisection_method
    elif choice == 2:
        method = ex_3_dagi.newton_raphson
    elif choice == 3:
        method = ex_3_dagi.secant_method
    else:
        print("Error")
    polynomial = sp.lambdify(x, polynomial)
    solution = []
    while start < end:
        if polynomial(start)*polynomial(start + 0.1) < 0:
            solution.append(method(polynomial, start, end))
        start += 0.1


x = sp.symbols('x')
polynomial = 0
start = 0
end = 0
input_data()
main()
