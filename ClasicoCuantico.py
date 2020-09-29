# Santiago Fetecua Suarez
# Libreria CNYT

from lib1 import *
import matplotlib.pyplot as plot
import numpy as np
import math


# PUNTO 1


def accbool(m1, v1):
    suma = 0
    mat = [0 for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                suma = suma + m1[i][k] * v1[k]
            if suma == 0:
                mat[i] = False
            else:
                mat[i] = True
    return mat


def canicas(m1, v1, n):
    if len(m1) == 0 or len(v1) == 0:
        print("Error")
    elif len(m1[0]) != len(v1):
        print("Error")
    else:
        conta = 1
        while conta <= n:
            vec = accbool(m1, v1)
            conta += 1
        return vec


# PUNTO 2


def accionNums(m1, v1):
    m = [[0 for i in range(len(v1[0]))] for j in range(len(m1))]
    for row in range(len(m1)):
        for column in range(len(v1[0])):
            for aux in range(len(m1[0])):
                m[row][column] = round((m[row][column] + (m1[row][aux] * v1[aux][column])), 3)
    return m


def sistClasico(m1, v1, n):
    if len(m1[0]) == len(v1) and len(m1[0]) == len(m1):
        while n > 0:
            v1 = accionNums(m1, v1)
            n -= 1
        return v1
    else:
        return -1


# PUNTO 3


def sistCuantico(m1, v1, n):
    if len(m1[0]) == len(v1) and len(m1[0]) == len(m1):
        while n > 0:
            v1 = accion(m1, v1)
            n -= 1
        for i in range(len(v1)):
            v1[i][0] = round(modulo(v1[i][0]) ** 2, 2)
        return v1
    else:
        return -1


# PUNTO 4


def grafica(vector):
    data = len(vector)
    x = np.array([x for x in range(data)])
    y = np.array([round(vector[x][0] * 100, 2) for x in range(data)])
    plot.bar(x, y, color='r', align='center')
    plot.title('Probabilidad')
    plot.show()
