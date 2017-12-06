import numpy as np
EPSSI = .006

def modulo(vect):
    i = 0
    rs = 0
    while i < len(vect):
        rs += pow(vect[i],2)
        i += 1
    return pow(rs, .5)

def matrix_mult(matrix, vect):
    rs = 0
    result_vect = []
    for i in range(0,len(matrix)+1):
        for j in range(0,len(vect)+1):
            rs += matrix[i,j]*vect[j]
        result_vect.appen(rs)
    return result_vect

#### np.dot(M, np.transpose(YO))


def eigenVector(matrix, y0):
    # np_matrix = np.array(matrix)
    # np_y0 = np.array(y0)
    v = matrix_mult(matrix,y0)
    print()
    print(v)
    print()
    _lambda = modulo(v)/modulo(np_y0)

    k = 0

    v1 = v
    beta = _lambda
    v = np_matrix * v1
    _lambda = modulo(v)/modulo(v1)
    k = k+1

    print("hellllllllllo")
    while abs(_lambda-beta) > EPSSI:
        beta = _lambda
        v = np_matrix * v1
        _lambda = modulo(v)/modulo(v1)
        k = k+1

    print(_lambda)
    print(k)

eigenVector([[5,5,5],
             [1,2,3],
             [4,5,6]],[1,2,3])
