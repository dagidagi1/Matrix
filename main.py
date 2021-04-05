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

def add_rows(row1,row2):
    return [row1[i] + row2[i] for i in range(len(row1))]

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

def init_id_mat(size):
    mat = []
    for i in range(size):
        new_row = []
        for j in range(size):
            if i == j:
                new_row.append(1)
            else:
                new_row.append(0)
        mat.append(new_row)
    return mat
def element_mat(size, row1_index, row2_index, multiplier):
    #row1 <-- row1 + multiplier * row2
    elem = init_id_mat(size)
    elem[row1_index] = add_rows(elem[row1_index], mul_row(elem[row2_index],multiplier))
    return elem

def find_singular(mat):
    size = len(mat)
    sing = init_id_mat(size)
    for piv in range(size):
            if mat[piv][piv] == 0:
                mat[piv], mat[piv + 1] = mat[piv + 1], mat[piv]
                sing[piv], sing[piv + 1] = sing[piv + 1], sing[piv]
            if mat[piv][piv] != 1:
                elem = init_id_mat(size)
                elem[piv][piv] = 1/mat[piv][piv] #pivot
                mat = mul_mat(elem, mat)
                sing = mul_mat(elem, sing)
            if piv != size:
                for i in range(piv + 1, size):
                    elem = element_mat(size, i, piv, -mat[i][piv])
                    mat, sing = mul_mat(elem, mat), mul_mat(elem, sing)
    for piv in range(size - 1, -1, -1):
            for i in range(piv - 1):
                elem = element_mat(size, i, piv, -mat[i][piv])
                mat, sing = mul_mat(elem, mat), mul_mat(elem, sing)
    return mat


def max_pivot_index(col):
    max_index = 0
    max = col[0]
    for i in range(len(col)):
        if max < col[i]:
            max = col[i]
            max_index = i
    return max_index

x = [[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]
print_mat(x)
print(determinant(x))
print_mat(find_singular(x))
#x1 = [[1,2,0],[4,3,-1]]
#x2 = [[5,1],[2,3],[3,4]]


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


def print_mat(mat):
    for i in mat:
        print(*i)


def way_A(mat, b):
    inv_mat = invert_mat(mat)
    return mul_mat(inv_mat, b)


def way_B(mat, b):
    l_mat = init_id_mat(len(mat))
    for j in range(len(mat)):  # columns
        m_mat = init_id_mat(len(mat))
        p_mat = init_id_mat(len(mat))
        for i in range(j, len(mat)):  # rows
            if i == j:
                max_piv = abs(mat[i][i])
                max_index = i
                for k in range(i+1, len(mat)):
                    if abs(mat[k][j]) > max_piv:
                        max_index = k
                        max_piv = abs(mat[k][j])
                if max_index != i:
                    mat[i], mat[max_index] = mat[max_index], mat[i]
                    p_mat[i], p_mat[max_index] = p_mat[max_index], p_mat[i]
            elif mat[i][j] != 0:
                m_mat[i][j] = -(mat[i][j]/mat[j][j])
        mat = mul_mat(m_mat, mat)
        l_mat = mul_mat(mul_mat(m_mat, p_mat), l_mat)
    temp_mat = mul_mat(l_mat, b)
    temp_mat = mul_mat(invert_mat(mat), temp_mat)
    return temp_mat


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
                if mat[i][j] == 0:
                    for k in range(i, len(mat)):
                        if mat[k][j] != 0:
                            elem_mat[k], elem_mat[i] = elem_mat[i], elem_mat[k]
                    mat = mul_mat(elem_mat, mat)
                    inv_mat = mul_mat(elem_mat, inv_mat)
                elif mat[i][j] == 1:
                    continue
                else:
                    elem_mat[i][j] = 1/mat[i][j]
                    mat = mul_mat(elem_mat, mat)
                    inv_mat = mul_mat(elem_mat, inv_mat)
            else:
                elem_mat[i][j] = -mat[i][j]/mat[j][j]
                mat = mul_mat(elem_mat, mat)
                inv_mat = mul_mat(elem_mat, inv_mat)
    for j in range(len(mat)-1, 0, -1):
        for i in range(j-1, -1, -1):
            elem_mat = init_id_mat(len(mat))
            elem_mat[i][j] = -mat[i][j]/mat[j][j]
            mat = mul_mat(elem_mat, mat)
            inv_mat = mul_mat(elem_mat, inv_mat)
    return inv_mat


def determinant(mat):
    def sub_mat_for_det(piv):
        def remove_row(x, i):
            new_mat = x.copy()
            new_mat.pop(i)
            return new_mat

        def remove_col(x, i):
            new_mat = x.copy()
            for _ in range(len(new_mat)):
                new_mat[_] = new_mat[_][:i] + new_mat[_][i + 1:]
            return new_mat
        new_mat = remove_row(mat, 0)
        new_mat = remove_col(new_mat, piv)
        return new_mat
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    sign = 1
    det = 0
    for i in range(len(mat[0])):
        det += sign * mat[0][i] * determinant(sub_mat_for_det(i))
        sign *= -1
    return det


mat_A, b = input_mat()
if determinant(mat_A) != 0:
    print_mat(way_A(mat_A, b))
else:
    print_mat(way_B(mat_A, b))
