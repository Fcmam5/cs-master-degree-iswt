import numpy as np
EPSSI = .006

def modulo(vect):
    i = 0
    rs = 0
    while i < len(vect):
        rs += pow(vect[i],2)
        i += 1
    return pow(rs, .5)

def eigenValue(matrix, y0):
    np_matrix = np.array(matrix)
    np_y0 = np.array(y0)
    v = np.dot(np_matrix, np.transpose(np_y0))
    _lambda = modulo(v)/modulo(np_y0)
    k = 0

    v1 = v
    beta = _lambda
    v = np_matrix * v1
    v = np.dot(np_matrix, np.transpose(v1))
    _lambda = modulo(v)/modulo(v1)
    k = k+1

    while abs(_lambda-beta) > EPSSI:
        beta = _lambda
        v = np.dot(np_matrix, np.transpose(v1))

        _lambda = modulo(v)/modulo(v1)
        k = k+1

    print(_lambda)
    print(k)

eigenValue([[5,5,5],
             [1,2,3],
             [4,5,6]],[1,1,1])
