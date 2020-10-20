# Santiago Fetecua Suarez
# Libreria CNYT
import math


def pp(a):
    if a[1] >= 0:
        print(a[0], "+", a[1], "i")
    else:
        print(a[0], a[1], "i")


def suma(a, b):
    res = (round(a[0] + b[0], 2), round(a[1] + b[1], 2))
    return res


def resta(a, b):
    return round(a[0] - b[0], 2), round(a[1] - b[1], 2)


def multi(a, b):
    res = ((a[0] * b[0]) - (a[1] * b[1]), (a[0] * b[1]) + (a[1] * b[0]))
    return res


def div(a, b):
    num1 = (a[0]*b[0]) + (a[1]*b[1])
    den = (b[0]**2) + (b[1]**2)
    num2 = (b[0]*a[1]) - (a[0]*b[1])
    return (num1/den), (num2/den)


def modulo(a):
    res = math.sqrt((a[0]**2) + (a[1]**2))
    return res


def conjugado(a):
    res = (a[0], (a[1]*-1))
    return res


def carteApolar(a):
    p = modulo(a)
    ang = math.atan(a[1]/a[0])
    return p, ang


def polarAcarte(c):
    x = c[0] * math.cos(c[1])
    y = c[0] * math.sin(c[1])
    return x, y


def fase(a):
    return math.atan2(a[1], a[0])


def addVect(a, b):
    return [suma(a[i], b[i]) for i in range(len(a))] if len(a) == len(b) else None


def inversoVect(a):
    n = (-1, 0)
    return [multi(a[i], n) for i in range(len(a))]


def multiEsc(n, a):
    return [multi(n, a[i]) for i in range(len(a))]


def addMatrix(a, b):
    return [addVect(a[i], b[i]) for i in range(len(a))] if len(a) == len(b) else None


def inversoMatrix(a):
    return [inversoVect(a[i]) for i in range(len(a))]


def multiEscMatrix(n, a):
    return [multiEsc(n, a[i]) for i in range(len(a))]


def transposeVhav(a):
    return [[a[i]] for i in range(len(a))]


def transposeVvah(a):
    return [a[i][0] for i in range(len(a))]


def transposeM(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


def conjugateVector(a):
    return [conjugado(a[i]) for i in range(len(a))]


def conjugateMatrix(a):
    return [conjugateVector(a[i]) for i in range(len(a))]


def adjointM(a):
    return conjugateMatrix(transposeM(a))


def multiMat(a, b):
    rowsA, columnsA = len(a), len(a[0])
    rowsB, columnsB = len(b), len(b[0])
    res = [[(0, 0) for j in range(columnsA)] for i in range(rowsA)]
    if columnsA == rowsB:
        for i in range(rowsA):
            for j in range(columnsB):
                for k in range(rowsB):
                    m = multi(a[i][k], b[k][j])
                    n = res[i][j]
                    res[i][j] = suma(m, n)
    return res


def accion(a, b):
    res = multiMat(a, b)
    for i in range(len(res)):
        res[i] = res[i][:1]
    return res


def innerProdcomplex(a, b):
    res = (0, 0)
    for i in range(len(a)):
        n = multi(conjugado(a[i]), b[i])
        res = suma(res, n)
    return res


def norm(a):
    a = innerProdcomplex(a, a)
    res = round(math.sqrt(a[0]), 2)
    return res


def distance(a, b):
    d = addVect(a, inversoVect(b))
    n = innerProdcomplex(d, d)
    res = round(math.sqrt(n[0]), 2)
    return res


def identity(m, n):
    matrix = [[(0, 0) for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j:
                matrix[i][j] = ((2/2), 0)
    return matrix


def unitaria(a):
    n = multiMat(adjointM(a), a)
    i = identity(len(a), len(a[0]))
    if n == i:
        return True
    else:
        return False


def hermitian(a):
    b = adjointM(a)
    if a == b:
        return True
    else:
        return False


def tensorproduct(a, b):
    try:
        rowsA, columnsA = len(a), len(a[0])
        rowsB, columnsB = len(b), len(b[0])
        m = rowsA * rowsB
        n = columnsA * columnsB
        res = [[[] for j in range(n)] for i in range(m)]
        for j in range(m):
            for k in range(n):
                res[j][k] = a[j//rowsB][k//columnsB] * b[j % rowsB][k % columnsB]
        return res
    except:
        m = len(a)
        n = len(b)
        size = m * n
        res = [[] for i in range(size)]
        for j in range(size):
            res[j] = a[j//n] * b[j % n]
        return res
