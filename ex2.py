from Ex1 import *
index = 0
def dominant_diagonal(mat, b):
    def extract_col(index):
        col = []
        for i in range(len(mat)):
            col.append(mat[i][index])
        return col
    def max_pivot_index(vec):
        #check if there is a pivot that greater than abs sum of other elements.
        #if no such element return (-1)
        max_index = -1
        vec_sum = sum(map(abs, vec))
        for i in range(len(vec)):
            if vec[i] > vec_sum - abs(vec[i]):
                max_index = i
        return max_index
    def swap_rows(mat, from_index, to_index):
        mat[to_index], mat[from_index] = mat[from_index], mat[to_index]
        return mat
    def swap_cols(from_index, to_index):
        for i in range(len(mat)):
            mat[i][from_index], mat[i][to_index] = mat[i][to_index], mat[i][from_index]
        return mat
    flag = True
    for i in range(len(mat)):
        col_pivot = max_pivot_index(mat[i][i:]) + i
        if col_pivot > i:
            swap_cols(col_pivot, i)
        if col_pivot == -1:
            flag = False
    return mat, flag


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
    d_mat = invert_mat(d_mat)#we use only inverted D.
    #yakobi G and H mats
    g_mat = minus_mat(mul_mat(d_mat, add_mat(l_mat, u_mat)))
    h_mat = d_mat
    #gaos G and H mats, dont work, dividing by zero error
    #g_mat =mul_mat(minus_mat(add_mat(l_mat,d_mat)), u_mat)
    #h_mat =invert_mat(add_mat(l_mat,d_mat))

    return step(init_def_vector(size))

x1= [[4,2,0],[0,4,5],[2,10,4]]
x2 = [[3,-1,1],[0,1,-1],[1,1,-2]]
#print_mat(yakobi(x1,[[2],[6],[5]]))
