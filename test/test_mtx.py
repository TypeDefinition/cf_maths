import unittest
import sys

# Why do I need to do this garbage to import a module that's right there?!
# Why can't this garbage shit-ass language just be normal?
# I fucking hate Python this is trash!
sys.path.insert(0, 'cf_maths')
from cf_maths.mtx import Mtx

class TestMtx(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Mtx(1, 1) != Mtx.identity(1), True)
        self.assertEqual(Mtx(2, 2) != Mtx.identity(2), True)
        self.assertEqual(Mtx(3, 3) != Mtx.identity(3), True)
        self.assertEqual(Mtx(4, 4) != Mtx.identity(4), True)

        self.assertNotEqual(Mtx(1, 1) == Mtx.identity(1), True)
        self.assertNotEqual(Mtx(2, 2) == Mtx.identity(2), True)
        self.assertNotEqual(Mtx(3, 3) == Mtx.identity(3), True)
        self.assertNotEqual(Mtx(4, 4) == Mtx.identity(4), True)

    def test_add(self):
        a = Mtx.from_array(2, 4, [2.0, 4.0, 7.0, 8.0, 2.0, 1.0, 0.0, 15.0])
        b = Mtx.from_array(2, 4, [15.0, 2.0, 1.0, 0.0, 0.0, 1.0, 77.0, 1045.0])
        c = Mtx.from_array(2, 4, [17.0, 6.0, 8.0, 8.0, 2.0, 2.0, 77.0, 1060.0])
        self.assertEqual(c == a + b, True)

    def test_sub(self):
        a = Mtx.from_array(2, 4, [2.0, 4.0, 7.0, 8.0, 2.0, 1.0, 0.0, 15.0])
        b = Mtx.from_array(2, 4, [15.0, 2.0, 1.0, 0.0, 0.0, 1.0, 77.0, 1045.0])
        c = Mtx.from_array(2, 4, [17.0, 6.0, 8.0, 8.0, 2.0, 2.0, 77.0, 1060.0])
        self.assertEqual(c - b == a, True)

    def test_mul(self):
        a = Mtx.from_array(1, 1, [4.0])
        b = Mtx.from_array(1, 1, [16.0])
        self.assertEqual(a * a == b, True)
        self.assertNotEqual(a * a == a, True)

        c = Mtx.from_array(4, 1, [1.0, 2.0, 3.0, 4.0])
        d = Mtx.from_array(1, 4, [1.0, 2.0, 3.0, 4.0])
        e = Mtx.from_array(1, 1, [30.0])
        self.assertEqual(c * d == e, True)

        f = Mtx.from_array(1, 3, [88.0, 45.0, -12.0])
        g = Mtx.from_array(3, 1, [-15.0, -103.0, 9.0])
        h = Mtx.from_array(3, 3, [-1320.0, -675.0, 180.0,
                                  -9064.0, -4635.0, 1236.0,
                                  792.0, 405.0, -108.0])
        self.assertEqual(f * g == h, True)

        i = Mtx.from_array(4, 4, [1.0, 2.0, 3.0, 4.0,
                                  5.0, 6.0, 7.0, 8.0,
                                  9.0, 10.0, 11.0, 12.0,
                                  13.0, 14.0, 15.0, 16.0])
        j = Mtx.from_array(4, 4, [17.0, 18.0, 19.0, 20.0,
                                  21.0, 22.0, 23.0, 24.0,
                                  25.0, 26.0, 27.0, 28.0,
                                  29.0, 30.0, 31.0, 32.0])
        k = Mtx.from_array(4, 4, [538.0, 612.0, 686.0, 760.0,
                                  650.0, 740.0, 830.0, 920.0,
                                  762.0, 868.0, 974.0, 1080.0,
                                  874.0, 996.0, 1118.0, 1240.0])
        self.assertEqual(i * j == k, True)
        self.assertEqual(k == i * j, True)
        self.assertNotEqual(k == j * i, True)
        self.assertEqual(i * Mtx.identity(4) == i, True)
        self.assertEqual(j * Mtx.identity(4) == j, True)
        self.assertEqual(i * Mtx.identity(4) != j, True)
        self.assertEqual(Mtx.identity(4) * k == k, True)
        self.assertEqual(Mtx.identity(4) * k == k * Mtx.identity(4), True)
        
    def test_transpose(self):
        a = Mtx.from_array(3, 2, [2.0, 4.0, 6.0, 8.0, 10.0, 12.0])
        b = Mtx.from_array(2, 3, [2.0, 6.0, 10.0, 4.0, 8.0, 12.0])
        self.assertEqual(a.transposed() == b, True)

        self.assertEqual(Mtx.identity(10).transposed() == Mtx.identity(10), True)

if __name__ == '__main__':
    unittest.main()

# TODO: Matrix Inverse