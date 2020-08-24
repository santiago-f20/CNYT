# Santiago Fetecua Suarez
# Test Libreria CNYT


import unittest
from lib1 import *


class TestStringMethods(unittest.TestCase):

    def testsuma(self):
        a = (2, 3)
        b = (3, 1)
        self.assertEqual(suma(a, b), (5, 4))

    def testresta(self):
        a = (3, -1)
        b = (1, 4)
        self.assertEqual(resta(a, b), (2, -5))

    def testmulti(self):
        a = (3, 2)
        b = (5, 6)
        self.assertEqual(multi(a, b), (3, 28))

    def testdiv(self):
        a = (1, 2)
        b = (2, 1)
        self.assertEqual(div(a, b), (4/5, 3/5))

    def testmodulo(self):
        a = (4, 3)
        self.assertEqual(modulo(a), 5)

    def testconjugado(self):
        a = (9, 5)
        self.assertEqual(conjugado(a), (9, -5))

    def testcarteApolar(self):
        a = (1, 1)
        self.assertEqual(carteApolar(a), (math.sqrt(2), math.pi/4))

    def testpolarAcarte(self):
        a = (10, (math.pi/6))
        self.assertEqual(polarAcarte(a), (8.660254037844387, 4.999999999999999))

    def testfase(self):
        a = (1, 1)
        self.assertEqual(fase(a), (math.pi/4))

    def testaddVect(self):
        a = [(6, -4), (7, 3), (4.2, -8.1), (0, -3)]
        b = [(16, 2.3), (0, -7), (6, 0), (0, -4)]
        self.assertEqual(addVect(a, b), [(22, -1.7), (7, -4), (10.2, -8.1), (0, -7)])

    def testinversoVect(self):
        a = [(8, -2), (5, 3), (6.5, -8.2), (0, -4)]
        self.assertEqual(inversoVect(a), [(-8, 2), (-5, -3), (-6.5, 8.2), (0, 4)])

    def testmultiEsc(self):
        n = (3, 2)
        a = [(6, 3), (0, 0), (5, 1), (4, 0)]
        self.assertEqual(multiEsc(n, a), [(12, 21), (0, 0), (13, 13), (12, 8)])

    def testaddMatrix(self):
        a = [(1, -4), (-2, 10), (4, 5)], [(-5, -9), (2, 2), (3, 0)]
        b = [(7, 15), (-9, -6), (5, 3)], [(8, 2), (4, -5), (-2, 20)]
        self.assertEqual(addMatrix(a, b), [[(8, 11), (-11, 4), (9, 8)], [(3, -7), (6, -3), (1, 20)]])

    def testinversoMatrix(self):
        a = [[(8, -2), (5, 3), (6.5, -8.2), (0, -4)], [(1, -2), (-2, 3), (4, -1), (-7, 9)]]
        self.assertEqual(inversoMatrix(a), [[(-8, 2), (-5, -3), (-6.5, 8.2), (0, 4)],
                                            [(-1, 2), (2, -3), (-4, 1), (7, -9)]])

    def testmultiEscMatrix(self):
        n = (3, 2)
        a = [[(6, 3), (0, 0), (5, 1), (4, 0)], [(4, -6), (1, 0), (-2, 9), (10, 8)]]
        self.assertEqual(multiEscMatrix(n, a), [[(12, 21), (0, 0), (13, 13), (12, 8)], [(24, -10), (3, 2), (-24, 23), (14, 44)]])

    def testtransposeM(self):
        a = [[(1, 9), (8, 1), (4, 2)], [(1, 2), (9, 0), (2, 3)], [(2, 3), (9, 7), (0, 0)]]
        self.assertEqual(transposeM(a), [[(1, 9), (1, 2), (2, 3)], [(8, 1), (9, 0), (9, 7)], [(4, 2), (2, 3), (0, 0)]])

    def testtransposeVhav(self):
        a = [(1, 2), (2, 3)]
        self.assertEqual(transposeVhav(a), [[(1, 2)], [(2, 3)]])

    def testtransposeVvah(self):
        a = [[(1, 2)], [(2, 3)]]
        self.assertEqual(transposeVvah(a), [(1, 2), (2, 3)])

    def testconjugateVector(self):
        a = [(2, 3), (5, -7), (1, 0), (4, 2)]
        self.assertEqual(conjugateVector(a), [(2, -3), (5, 7), (1, 0), (4, -2)])

    def testconjugateMatrix(self):
        a = [[(3, 4), (1, 2)], [(1, 0), (0, -8)]]
        self.assertEqual(conjugateMatrix(a), [[(3, -4), (1, -2)], [(1, 0), (0, 8)]])

    def testadjointM(self):
        a = [[(1, -1), (0, 0)], [(3, 4), (-1, 0)]]
        self.assertEqual(adjointM(a), [[(1, 1), (3, -4)], [(0, 0), (-1, 0)]])

    def testmultiMat(self):
        a = [[(3, 2), (0, 0), (5, -6)], [(1, 0), (4, 2), (0, 1)], [(4, -1), (0, 0), (4, 0)]]
        b = [[(5, 0), (2, -1), (6, -4)], [(0, 0), (4, 5), (2, 0)], [(7, -4), (2, 7), (0, 0)]]
        self.assertEqual(multiMat(a, b), [[(26, -52), (60, 24), (26, 0)], [(9, 7), (1, 29), (14, 0)], [(48, -21), (15, 22), (20, -22)]])

    def testaccion(self):
        a = [[(-1, 0), (1, 1), (0, 0)], [(2, -1), (0, 0), (1, 0)], [(0, 0), (1, -1), (0, 1)]]
        b = [[(1, 0)], [(1, 1)], [(0, 1)]]
        self.assertEqual(accion(a, b), [[(-1, 2)], [(2, 0)], [(1, 0)]])

    def testinnerProdcomplex(self):
        a = [(2, 3), (1, 2)]
        b = [(0, 2), (1, 2)]
        self.assertEqual(innerProdcomplex(a, b), (11, 4))

    def testnorm(self):
        a = [(3, 2), (5, -6), (-2, 8)]
        self.assertEqual(norm(a), 11.92)

    def testdistance(self):
        a = [(4, 2), (5, 7), (9, 1)]
        b = [(8, 3), (3, 8), (2, 5)]
        self.assertEqual(distance(a, b), 9.33)

    def testunitaria(self):
        a = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]
        b = [[(1, 2), (3, 0)], [(6, 4), (5, -8)]]
        self.assertEqual(unitaria(a), True)
        self.assertEqual(unitaria(b), False)

    def testhermitian(self):
        a = [[(5, 0), (4, 5), (6, -16)], [(4, -5), (13, 0), (7, 0)], [(6, 16), (7, 0), (-2.1, 0)]]
        b = [[(4, 0), (3, 8)], [(6, -10), (5, -7)]]
        self.assertEqual(hermitian(a), True)
        self.assertEqual(hermitian(b), False)

    def testtensorproduct(self):
        a = [[3, 2, 4], [2, 5, 7]]
        b = [[1, 2, -3], [9, -6, 2], [8, 3, -6]]
        self.assertEqual(tensorproduct(a, b), [[3, 6, -9, 2, 4, -6, 4, 8, -12], [27, -18, 6, 18, -12, 4, 36, -24, 8],
                                              [24, 9, -18, 16, 6, -12, 32, 12, -24], [2, 4, -6, 5, 10, -15, 7, 14, -21],
                                              [18, -12, 4, 45, -30, 10, 63, -42, 14], [16, 6, -12, 40, 15, -30, 56, 21, -42]])


if __name__ == '__main__':
    unittest.main()
