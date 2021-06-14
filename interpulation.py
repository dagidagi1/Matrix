#Arkadi Yakubov 208064162
#Mikhail diachkov 336426176
from Ex1 import print_mat
def mat_solve(mat, vec_b):
    def init_id_mat(size):
        id_mat = []
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            id_mat.append(row)
        return id_mat

    def mul_mat(mat1, mat2):
        def get_col(mat, i):
            col = []
            for _ in mat:
                col.append(_[i])
            return col

        def mul_row_col(row, col):
            x = 0
            for i in range(len(row)):
                x += row[i] * col[i]
            return x

        if len(mat1[0]) != len(mat2):
            print("Can't multiply this matrix!")
            return None
        new_mat = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2[0])):
                row.append(mul_row_col(mat1[i], get_col(mat2, j)))
            new_mat.append(row)
        return new_mat
    def invert_mat(mat):
        inv_mat = init_id_mat(len(mat))
        for j in range(len(mat)):
            for i in range(j, len(mat)):
                elem_mat = init_id_mat(len(mat))
                if i == j:
                    max_piv = abs(mat[i][i])
                    max_index = i
                    for k in range(i + 1, len(mat)):
                        if abs(mat[k][j]) > max_piv:
                            max_index = k
                            max_piv = abs(mat[k][j])
                    if max_index != i:
                        mat[i], mat[max_index] = mat[max_index], mat[i]
                        inv_mat[i], inv_mat[max_index] = inv_mat[max_index], inv_mat[i]
                    elem_mat[i][i] = 1 / mat[i][i]
                    mat = mul_mat(elem_mat, mat)
                    inv_mat = mul_mat(elem_mat, inv_mat)
                else:
                    elem_mat[i][j] = -mat[i][j] / mat[j][j]
                    mat = mul_mat(elem_mat, mat)
                    inv_mat = mul_mat(elem_mat, inv_mat)
        for j in range(len(mat) - 1, 0, -1):
            for i in range(j - 1, -1, -1):
                elem_mat = init_id_mat(len(mat))
                elem_mat[i][j] = -mat[i][j] / mat[j][j]
                mat = mul_mat(elem_mat, mat)
                inv_mat = mul_mat(elem_mat, inv_mat)
        return inv_mat
    inv_mat = invert_mat(mat)
    return mul_mat(inv_mat, vec_b)

def linear_interpulation(points, x_f):

    # points is a list of lists -> [[x1, y1], [x2, y2], ....]
    # x = x value of the point we need to find.

    def nearest_points(x_f, points):
        if len(points) == 2:
            return points[0], points[1]
        if len(points) < 2:
            print("Not enough points!!!\n")
            return False
        points.sort(key=lambda x: x[0]) #sorting points by x value from small --> big

        if points[0][0] > x_f:
            p1,p2 = points[0], points[1]
        if points[-1][0] < x_f:
            p2, p1 = points[-1], points[-2]
            return p1,p2
        for i in range(len(points)):
            if points[i][0] > x_f:
                p2, p1 = points[i], points[i - 1]
                break
        return p1, p2

    p1, p2 = nearest_points(x_f, points)
    print("Linear interpulation used this 2 points: ",p1,p2)
    return ( (x_f - p2[0]) / (p1[0] - p2[0]) ) * p1[1] + ( (x_f - p1[0]) / (p2[0] - p1[0]) ) * p2[1]


def polynomial_interpulation(points, x_f):
    poly_deg = len(points) - 1
    p_x = 0.0
    mat = []
    vec_b = []
    for p in points:
        row = []
        for deg in range(poly_deg + 1):
            row.append(p[0] ** deg)
        row.reverse()
        mat.append(row)
        vec_b.append([p[1]])
    print("Polynomial Equation coefficients matrix:")
    print_mat(mat)
    factor_vec = mat_solve(mat, vec_b)
    for fac in factor_vec:
        p_x += fac[0] * (x_f**poly_deg)
        poly_deg -= 1
    return p_x


def neville_interpulation(points, x_f):
    def poly(m, n):
        print("Neville interpulation number: ",m,n)
        if m == n:
            if points[m][0] == x_f:
                return points[m][1]
            else:
                return points[n][1]
        return (((x_f - points[m][0]) * poly(m + 1, n)) - ((x_f - points[n][0]) * poly(m, n - 1))) \
               / (points[n][0] - points[m][0])
    return poly(0,len(points) - 1)

def lagrange_interpulation(points, x):
    res = 0
    for i in range(len(points)):
        numerator = 1
        denomerator = 1
        for j in range(len(points)):
            if i != j:
                numerator *= x - points[j][0]
                denomerator *= points[i][0] - points[j][0]
        res += (numerator*points[i][1])/denomerator
    return res

def main():

    points = []
    print("Please insert amount of table points:")
    amount = int(input())
    for i in range(amount):
        point = []
        print("X[{0}] = ".format(i), end= '')
        point.append(float(input()))
        print("\nY[{0}] = ".format(i), end='')
        point.append(float(input()))
        points.append(point)
    print("X value of the point we are looking for:")
    x_f = float(input())
    print("Please enter method number: "
          "\n1)Linear interpulation"
          "\n2)Neville interpulation"
          "\n3)Polynomial interpulation"
          "\n4)Lagrange interpulation")
    choice = int(input())
    method = None
    if choice == 1:
        method = linear_interpulation
    elif choice == 2:
        method = neville_interpulation
    elif choice == 3:
        method = polynomial_interpulation
    elif choice == 4:
        method = lagrange_interpulation

    else:
        print("Bad input")
    print(method(points, x_f))

main()