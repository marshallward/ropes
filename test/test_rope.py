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
        s = 'abc'
        r = Rope(s)
        for i in range(-len(s), len(s)):
            self.assertEqual(Rope(s[i]), r[i])

        for i in range(len(s), 3 * len(s)):
            self.assertRaises(IndexError, r.__getitem__, i)
            self.assertRaises(IndexError, r.__getitem__, -(i + 1))

    def test_slice_onenode(self):
        s = 'abc'
        r = Rope(s)

        for i in range(-(len(s) + 2), len(s) + 2):
            self.assertEqual(Rope(s[:i]), r[:i])

        for i in range(-(len(s) + 2), len(s) + 2):
            self.assertEqual(Rope(s[i:]), r[i:])

    def test_index_threenode(self):
        s = 'abcde'

        r0 = Rope(s[:2])
        r1 = Rope(s[2:])
        r = r0 + r1

        for i in range(-len(s), len(s)):
            self.assertEqual(Rope(s[i]), r[i])

        for i in range(len(s), 3 * len(s)):
            self.assertRaises(IndexError, r.__getitem__, i)
            self.assertRaises(IndexError, r.__getitem__, -(i + 1))

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
