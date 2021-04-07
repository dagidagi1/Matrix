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
    for i in range(len(mat)):
        for j in mat[i]:
            print("%.3f" % j, end="\t")
        print()


def way_A(mat, b):
    inv_mat = invert_mat(mat)
    return mul_mat(inv_mat, b)


def lu_dec(mat):
    l_mat = init_id_mat(len(mat))
    for j in range(len(mat)):  # columns
        m_mat = init_id_mat(len(mat))
        for i in range(j, len(mat)):  # rows
            if i == j:
                if mat[i][i] == 0:
                    for k in range(i+1, len(mat)):
                        if mat[k][j] != 0:
                            m_mat[i], m_mat[k] = m_mat[k], m_mat[i]
                            mat = mul_mat(m_mat, mat)
                            l_mat = mul_mat(m_mat, l_mat)
                            m_mat = init_id_mat(len(mat))
                            break
            else:
                m_mat[i][j] = -(mat[i][j]/mat[j][j])
        mat = mul_mat(m_mat, mat)
        l_mat = mul_mat(m_mat, l_mat)
    return invert_mat(l_mat), mat


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
                elem_mat[i][i] = 1/mat[i][i]
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


def example():
    '''Matrix is stored in list of row_lists.

    '''
    example_mat = x = [[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]
    vector_b = [[1],[2],[3],[4]]
    print("example matrix(can be changed in the code):\n")
    print_mat(example_mat)
    if determinant(example_mat) == 0:
        print("determinant of the matrix is 0, cant find inverted matrix.")
        l_mat, u_mat = lu_dec(example_mat)
        print("===========================================")
        print("L matrix:\n")
        print_mat(l_mat)
        print("===========================================")
        print("U matrix:\n")
        print_mat(u_mat)
        print("===========================================")
        print("L * U matrix:\n")
        print_mat(mul_mat(l_mat, u_mat))
        return
    else:
        print("===========================================")
        print("example vector b(can be changed in the code):\n")
        print_mat(vector_b)
        print("===========================================")
        print("A_inv * b:\n")
        print_mat(mul_mat(invert_mat(example_mat), vector_b))


example()

