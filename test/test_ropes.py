import sys
import unittest

sys.path.insert(1, '../')
from ropes import Rope

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

    def test_list(self):
        self.assertEqual(Rope(), Rope([]))
        self.assertEqual(Rope('abc'), Rope(['abc']))
        self.assertEqual(Rope('ab') + Rope('cd'), Rope(['ab', 'cd']))
        self.assertEqual(Rope('a') + Rope('b') + Rope('c'),
                         Rope(['a', 'b', 'c']))

        s = 'These are some words'.split()
        r = (Rope('These') + Rope('are')) + (Rope('some') + Rope('words'))
        self.assertEqual(r, Rope(s))

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

        for i in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(Rope(s[:i]), r[:i])

        for i in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(Rope(s[i:]), r[i:])

        # TODO: Test interior strides (combine all into double loop)

    def test_index_threenode(self):
        s = 'abcde'
        r = Rope('abc') + Rope('de')

        for i in range(-len(s), len(s)):
            self.assertEqual(Rope(s[i]), r[i])

        for i in range(len(s), 3 * len(s)):
            self.assertRaises(IndexError, r.__getitem__, i)
            self.assertRaises(IndexError, r.__getitem__, -(i + 1))

    def test_slice_threenode(self):
        s = 'abc' + 'de'
        r = Rope('abc') + Rope('de')

        # TODO: Condense this
        self.assertEqual(Rope('abc') + Rope('de'), r[:])

        self.assertEqual(Rope(''), r[:0])
        self.assertEqual(Rope('a'), r[:1])
        self.assertEqual(Rope('ab'), r[:2])
        self.assertEqual(Rope('abc'), r[:3])
        self.assertEqual(Rope('abc') + Rope('d'), r[:4])
        self.assertEqual(Rope('abc') + Rope('de'), r[:5])

        for i in range(len(s) + 1, 3 * len(s)):
            self.assertEqual(Rope('abc') + Rope('de'), r[:i])

        self.assertEqual(Rope('abc') + Rope('d'), r[:-1])
        self.assertEqual(Rope('abc'), r[:-2])
        self.assertEqual(Rope('ab'), r[:-3])
        self.assertEqual(Rope('a'), r[:-4])
        self.assertEqual(Rope(''), r[:-5])

        for i in range(-3 * len(s), -len(s) - 1):
            self.assertEqual(Rope(''), r[:i])

        self.assertEqual(Rope('abc') + Rope('de'), r[0:])
        self.assertEqual(Rope('bc') + Rope('de'), r[1:])
        self.assertEqual(Rope('c') + Rope('de'), r[2:])
        self.assertEqual(Rope('de'), r[3:])
        self.assertEqual(Rope('e'), r[4:])
        self.assertEqual(Rope(''), r[5:])

        for i in range(len(s) + 1, 3 * len(s)):
            self.assertEqual(Rope(''), r[i:])

        self.assertEqual(Rope('e'), r[-1:])
        self.assertEqual(Rope('de'), r[-2:])
        self.assertEqual(Rope('c') + Rope('de'), r[-3:])
        self.assertEqual(Rope('bc') + Rope('de'), r[-4:])
        self.assertEqual(Rope('abc') + Rope('de'), r[-5:])

        for i in range(-3 * len(s), -len(s) - 1):
            self.assertEqual(Rope('abc') + Rope('de'), r[i:])

    def test_word_iteration(self):
        words = ['a', 'b', 'c', 'd', 'e']
        rope = Rope(words)
        for i, w in enumerate(rope):
            self.assertEqual(w, words[i])

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
