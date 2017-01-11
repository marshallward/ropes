import sys
import unittest

sys.path.insert(1, '../')
from rope import Rope

class Test(unittest.TestCase):

    def setUp(self):
        # TODO: targets
        pass

    def test_empty(self):
        r = Rope()
        self.assertEqual(None, r.left)
        self.assertEqual(None, r.right)
        self.assertEqual(0, r.length)
        self.assertEqual('', r.data)

    def test_index_onenode(self):
        r = Rope('abc')
        self.assertEqual(Rope('a'), r[0])
        self.assertEqual(Rope('b'), r[1])
        self.assertEqual(Rope('c'), r[2])

        self.assertEqual(Rope('c'), r[-1])
        self.assertEqual(Rope('b'), r[-2])
        self.assertEqual(Rope('a'), r[-3])

        # Is there a better way to do this?
        self.assertRaises(IndexError, r.__getitem__, 3)
        self.assertRaises(IndexError, r.__getitem__, -4)

    def test_index_threenode(self):
        r = Rope('ab')
        s = Rope('cd')
        t = r + s

        self.assertEqual(Rope('a'), t[0])
        self.assertEqual(Rope('b'), t[1])
        self.assertEqual(Rope('c'), t[2])
        self.assertEqual(Rope('d'), t[3])

        self.assertEqual(Rope('d'), t[-1])
        self.assertEqual(Rope('c'), t[-2])
        self.assertEqual(Rope('b'), t[-3])
        self.assertEqual(Rope('a'), t[-4])

        self.assertRaises(IndexError, r.__getitem__, 4)
        self.assertRaises(IndexError, r.__getitem__, -5)

    def test_equality(self):
        r = Rope('a') + Rope('b') + Rope('c')
        s = Rope('a') + (Rope('b') + Rope('c'))
        t = (Rope('a') + Rope('b')) + Rope('c')
        u = Rope('abc')

        self.assertNotEqual(r, s)
        self.assertEqual(r, t)
        self.assertNotEqual(r, u)


if __name__ == '__main__':
    unittest.main()
