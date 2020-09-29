# Santiago Fetecua Suarez
# Test Libreria CNYT


import unittest
from ClasicoCuantico import *


class TestClasicoCuantico(unittest.TestCase):

    def testCanicas(self):
        m1 = [[False, False, False, False, False, False], [False, False, False, False, False, False],
              [False, True, False, False, False, True],
              [False, False, False, True, False, False], [False, False, True, False, False, False],
              [True, False, False, False, True, False]]
        v1 = [True, True, True, True, True, True]
        n = 2
        self.assertEqual(canicas(m1, v1, n), [False, False, True, True, True, True])

    def testSistClasico(self):
        m1 = [[0, 1/6, 5/6], [1/3, 1/2, 1/6], [2/3, 1/3, 0]]
        v1 = [[1/6], [1/6], [2/3]]
        n = 3
        self.assertEqual(sistClasico(m1, v1, n), [[0.451], [0.313], [0.237]])

    def testSistCuantico(self):
        m1 = [[(1 / math.sqrt(2), 0), (0, 1 / math.sqrt(2))], [(1 / math.sqrt(2), 0), (0, -1 / math.sqrt(2))]]
        v1 = [[(1, 0)], [(0, 0)]]
        m2 = [[(1 / math.sqrt(2), 0), (1 / math.sqrt(2), 0), (0, 0)],
              [(0, -1 / math.sqrt(2)), (0, 1 / math.sqrt(2)), (0, 0)],
              [(0, 0), (0, 0), (0, -1)]]
        v2 = [[(1 / math.sqrt(3), 0)], [(0, 2 / math.sqrt(15))], [(math.sqrt(2 / 5), 0)]]
        self.assertEqual(sistCuantico(m1, v1, 1), [[0.5], [0.5]])
        self.assertEqual(sistCuantico(m2, v2, 4), [[0.3], [0.3], [0.4]])


if __name__ == '__main__':
    unittest.main()
