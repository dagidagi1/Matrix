#Arkadi Yakubov 208064162
#Mikhail diachkov 336426176
from Ex1 import *
def input_mat():
    x = int(input("Please enter matrix size: "))
    mat = []
    for row in range(x):
        row_list = []
        for col in range(x):
            row_list.append(float(input("row: {0} col : {1}......".format(row+1, col+1))))
        mat.append(row_list)
    b = []
    print('Enter b-vector:')
    for i in range(x):
        temp = [float(input())]
        b.append(temp)
    return mat, b


def print_mat(mat, b):
    for i in range(len(mat)):
        for j in mat[i]:
            print("%.3f" % j, end="\t")
        print("%.3f" % b[i][0])


def dominant_diagonal(mat, b):
    def check_row(index1, index2):
        row_sum = -abs(mat[index1][index2])
        for j in range(len(mat)):
            row_sum += abs(mat[index1][j])
        if abs(mat[index1][index2]) >= row_sum:
            return True
        return False

    def check_diagonal():
        for i in range(len(mat)):
            if not check_row(i, i):
                print("There is no dominant diagonal!")
                return False
        return True

    def swap_rows():
        nonlocal mat, b
        for i in range(len(mat) - 1):
            for j in range(i, len(mat)):
                if check_row(j, i):
                    if i != j:
                        mat[i], mat[j] = mat[j], mat[i]
                        b[i], b[j] = b[j], b[i]

    swap_rows()
    return check_diagonal()


def yakobi(mat, vec_b):
    global epsilon
    size = len(mat)
    index = 0
    def print_iteration(index, vec):
        print(index, end=" | ")
        for i in range(len(vec)):
            print("%.3f" % vec[i][0], end="\t")
        print()
    def init_zero_mat(size):
        mat = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            mat.append(row)
        return mat
    def init_def_vector(size):
        vec = []
        for i in range(size):
            row = [0]
            vec.append(row)
        return vec
    def decomposition(mat):
        #returns U matrix, L matrix, D matrix
        d_mat = init_zero_mat(size)
        u_mat = init_zero_mat(size)
        l_mat = init_zero_mat(size)
        for i in range(size):
            for j in range(size):
                if j == i:
                    d_mat[i][j] = mat[i][j]
                elif j<i:
                    l_mat[i][j] = mat[i][j]
                else:
                    u_mat[i][j] = mat[i][j]
        return u_mat, l_mat, d_mat
    def add_mat(mat1, mat2):
        new_mat = mat1
        for i in range(len(mat1)):
            for j in range(len(mat1[i])):
                new_mat[i][j] += mat2[i][j]
        return new_mat
    def minus_mat(mat):
        for i in range(size):
            for j in range(len(mat[i])):
                if mat[i][j] != 0:
                    mat[i][j] = -mat[i][j]
        return mat
    def check_eps(vec1, vec2):
        for i in range(len(vec1)):
            if abs(vec2[i][0] - vec1[i][0]) > epsilon:
                return False
        return True
    def step(x_r):
        nonlocal index
        index += 1
        next_x_r = add_mat(mul_mat(g_mat, x_r), mul_mat(h_mat, vec_b))
        print_iteration(index, next_x_r)
        if(check_eps(x_r, next_x_r)):
            return next_x_r
        return step(next_x_r)

    u_mat, l_mat, d_mat = decomposition(mat)
    d_mat = invert_mat(d_mat)#we use only inverted D.
    #yakobi G and H mats
    g_mat = minus_mat(mul_mat(d_mat, add_mat(l_mat, u_mat)))
    h_mat = d_mat
    #gaos G and H mats, dont work, dividing by zero error
    #g_mat =mul_mat(minus_mat(add_mat(l_mat,d_mat)), u_mat)
    #h_mat =invert_mat(add_mat(l_mat,d_mat))
    print("", end="\t")
    for i in range(size):
        print(f"X{i + 1}", end="\t\t")
    print()
    return step(init_def_vector(size))


def gauss_seidel(mat, b):
    def make_new_mat():
        new_mat = []
        for i in range(len(mat)):
            row = [b[i][0]/mat[i][i]]
            for j in range(len(mat)):
                if i == j:
                    row.append(0)
                else:
                    row.append(mat[i][j]/(-mat[i][i]))
            new_mat.append(row)
        return new_mat

    def check_epsilon(vec1, vec2):
        for i in range(len(vec1)):
            if abs(vec1[i] - vec2[i]) > epsilon:
                return False
        return True

    def check_squeeze(vec1, vec2):
        for i in range(len(vec1)):
            if abs(vec1[i] - vec2[i]) > 100:
                return True
        return False

    x = []
    x_1 = []
    for i in range(len(mat)):
        x.append(0)
        x_1.append(0)
    new_mat = make_new_mat()
    print("", end="\t")
    for i in range(len(new_mat)):
        print(f"X{i+1}", end="\t\t")
    print()
    attempt = 0
    while True:
        for i in range(len(new_mat)):
            x_1[i] += new_mat[i][0]
            for j in range(1, i+1):
                x_1[i] += new_mat[i][j]*x_1[j-1]
            for j in range(i+1, len(new_mat)+1):
                x_1[i] += new_mat[i][j]*x[j-1]
        print(f"{attempt+1} | ", end="")
        for i in x:
            print("%.3f" % i, end="\t")
        print()
        if check_epsilon(x, x_1):
            attempt += 1
            if not solvable:
                print("However there is no dominant diagonal,")
            print(f"Solved in {attempt} attempts")
            return x_1
        if not solvable:
            if check_squeeze(x, x_1):
                print("Problem can't be solved")
                return False
        x = x_1.copy()
        for i in range(len(x_1)):
            x_1[i] = 0
        attempt += 1


def main():
    global epsilon, mat, b, solvable
    user_input = int(input("Hello,\n1 - Use default values\n2 - Enter new values\nEnter your choice: "))
    if user_input == 2:
        mat, b = input_mat()
        epsilon = float(input("Enter epsilon: "))
    else:
        epsilon = 0.00001
        mat = [[-2, 2, 1], [1, 3, 2], [1, -2, 0]]
        b = [[1], [4], [6]]
    solvable = dominant_diagonal(mat, b)
    print_mat(mat, b)
    print("Jacobi:")
    yakobi(mat, b)
    print("Gauss Seidel:")
    gauss_seidel(mat, b)


epsilon = 0
mat = []
b = []
solvable = True
main()



