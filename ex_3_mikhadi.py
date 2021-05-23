import sympy as sp

x = sp.symbols('x')
func = 0
deg = int(input("Which degree of function?: "))
print("Enter function")
for i in range(deg, -1, -1):
    t = float(input(f"(x**{i})*"))
    func += t*x**i
print(f"Your func: {func}")
