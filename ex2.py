from Ex1 import *

index = 0
def yakobi(mat, vec_b):
    eps = 0.00001
    size = len(mat)
    def print_iteration(index, vec):
        print(index, end = " | ")
        for i in range(len(vec)):
            print("%.6f" % vec[i][0], end = "\t")
        print("\n")

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
            if abs(vec2[i][0] - vec1[i][0]) > eps:
                return False
        return True
    def step(x_r):
        global index
        index += 1
        next_x_r = add_mat(mul_mat(g_mat, x_r), mul_mat(h_mat, vec_b))
        print_iteration(index, next_x_r)
        if(check_eps(x_r, next_x_r)):
            return next_x_r
        return step(next_x_r)

    u_mat, l_mat, d_mat = decomposition(mat)
    d_mat = invert_mat(d_mat)
    #yakobi
    g_mat = minus_mat(mul_mat(d_mat, add_mat(l_mat, u_mat)))
    h_mat = d_mat
    #gaos
    #g_mat =mul_mat(minus_mat(add_mat(l_mat,d_mat)), u_mat)
    #h_mat =invert_mat(add_mat(l_mat,d_mat))
    print_mat(step(init_def_vector(size)))

x1= [[4,2,0],[2,10,4],[0,4,5]]
x2 = [[3,-1,1],[0,1,-1],[1,1,-2]]
yakobi(x2,[[4],[-1],[-3]])
