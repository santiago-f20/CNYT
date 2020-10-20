# Santiago Fetecua Suarez
# Libreria CNYT

from lib1 import *
from ClasicoCuantico import *
from numpy import linalg as Alg


def normaVectorial(a):
    res = 0
    for i in a:
        res += modulo(i)**2
    return res**0.5

def prob_pos_v(v,x):
    return modulo(v[x][0])**2/normaVectorial(transposeVvah(v))**2


def prob_pos_h(v,x):
    return modulo(v[x])**2/cal.normaVectorial(v)**2


def valor_esperado(sistema,omega):
    a = multiMat(omega,sistema)
    for i in range(len(a)):
        print(a[i])
    return innerProdcomplex(a,sistema)


