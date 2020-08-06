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
        self.assertEqual(modulo(a), (5))

    def testconjugado(self):
        a = (9, 5)
        self.assertEqual(conjugado(a), (9, -5))

    def testcarteApolar(self):
        a = (1, 1)
        self.assertEqual(carteApolar(a), (math.sqrt(2), math.pi/4))

    def testpolarAcarte(self):
        a = (math.sqrt(2), (math.pi/4))
        self.assertEqual(polarAcarte(a), (1.0000000000000002, 1.0000000000000002))

    def fase(self):
        a = (1, 1/2)
        self.assertEqual(fase(a), (math.pi/2))

if __name__ == '__main__':
    unittest.main()
