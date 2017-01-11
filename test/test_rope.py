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


if __name__ == '__main__':
    unittest.main()
