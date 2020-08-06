import math


def suma(a, b):
    res = (a[0]+b[0], a[1]+b[1])
    return res


def resta(a, b):
    return (a[0]-b[0], a[1]-b[1])


def multi(a, b):
    res = ((a[0]*b[0]) - (a[1]*b[1]), (a[0]*b[1]) + (a[1]*b[0]))
    return(res)


def div(a, b):
    num1 = (a[0]*b[0]) + (a[1]*b[1])
    den = (b[0]**2) + (b[1]**2)
    num2 = (b[0]*a[1]) - (a[0]*b[1])
    return ((num1/den), (num2/den))


def modulo(a):
    res = math.sqrt((a[0]**2) + (a[1]**2))
    return res


def conjugado(a):
    res = (a[0], (a[1]*-1))
    return res


def carteApolar(a):
    p = math.sqrt((a[0])**2+(a[1]**2))
    ang = math.atan(a[1]/a[0])
    return p, ang


def polarAcarte(c):
    a = c[0] * math.cos(c[1])
    b = c[0] * math.sin(c[1])
    return a, b


def fase(a):
    c = carteApolar(a)
    return c[1]
