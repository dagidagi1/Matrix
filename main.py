def input_mat():
    x = input("Please enter matrix size: ")
    mat = []
    row_list = []
    for row in range(x):
        for col in range(x):
            row_list[col] = input("row: {0} col : {1}......".format(row,col))
        mat[row] = row_list
    return mat


def print_mat(mat):
    for i in mat:
        print(*i)


def sub_mat_for_det(mat, piv):
    new_mat = remove_row(mat, 0)
    new_mat = remove_col(new_mat,piv)
    return new_mat


def determinant(mat):
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    sign = 1
    det = 0
    for i in range(len(mat[0])):
        det += sign * mat[0][i] * determinant(sub_mat_for_det(mat,i))
        sign *= -1
    return det


def remove_row(x, i):
    new_mat = x.copy()
    new_mat.pop(i)
    return new_mat


def remove_col(x, i):
    new_mat = x.copy()
    for _ in range(len(new_mat)):
        new_mat[_] = new_mat[_][:i] + new_mat[_][i+1 :]
    return new_mat


def mul_row(row, multiplier):
    return [i * multiplier for i in row]


def get_col(mat, i):
    col = []
    for _ in mat:
      col.append(_[i])
    return col


def mul_row_col(row,col):
    x = 0
    for i in range(len(row)):
        x += row[i]*col[i]
    return x


def mul_mat(mat1,mat2):
    if len(mat1[0]) != len(mat2):
        print("cant multiply this matrix!")
        return None
    new_mat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            row.append(mul_row_col(mat1[i],get_col(mat2, j)))
        new_mat.append(row)
    return new_mat


def max_pivot_index(col):
    max_index = 0
    max = col[0]
    for i in range(len(col)):
        if max < col[i]:
            max = col[i]
            max_index = i
    return max_index

x = [[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]
#print_mat(x)
#print(determinant(x))

x1 = [[1,2,0],[4,3,-1]]
x2 = [[5,1],[2,3],[3,4]]