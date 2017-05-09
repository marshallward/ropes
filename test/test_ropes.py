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
        s = 'abcdefg'
        r = Rope(s)

        # Implicit start, step
        for i in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(Rope(s[:i]), r[:i])

        # Implicit stop, step
        for i in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(Rope(s[i:]), r[i:])

        # Explicit slices
        for i in range(-3 * len(s), 3 * len(s)):
            for j in range(-3 * len(s), 3 * len(s)):
                for k in range(1, len(s)):
                    self.assertEqual(s[i:j:k], str(r[i:j:k]))

    def test_index_threenode(self):
        s = 'abcde'
        r = Rope('abc') + Rope('de')

        for i in range(-len(s), len(s)):
            self.assertEqual(Rope(s[i]), r[i])

        for i in range(len(s), 3 * len(s)):
            self.assertRaises(IndexError, r.__getitem__, i)
            self.assertRaises(IndexError, r.__getitem__, -(i + 1))

    def test_slice_threenode(self):
        # Isn't this included in the other test now?
        s = 'abc' + 'de'
        r = Rope('abc') + Rope('de')

        # TODO: Condense this
        self.assertEqual(Rope('abc') + Rope('de'), r[:])

        for i in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(s[i:], str(r[i:]))

        for j in range(-3 * len(s), 3 * len(s)):
            self.assertEqual(s[:j], str(r[:j]))

        for i in range(-3 * len(s), 3 * len(s)):
            for j in range(-3 * len(s), 3 * len(s)):
                self.assertEqual(s[i:j], str(r[i:j]))

    def test_stride_threenode(self):
        s = 'abcde' + 'fghijkl'
        r = Rope(['abcde', 'fghijkl'])

        for i in range(-3 * len(s), 3 * len(s)):
            for k in range(0, len(s) + 1):
                if k == 0:
                    self.assertRaises(ValueError, r.__getitem__,
                                      slice(i,None,k))
                else:
                    self.assertEqual(s[i::k], str(r[i::k]))
                    self.assertEqual(s[:i:k], str(r[:i:k]))

        for i in range(-3 * len(s), 3 * len(s)):
            for j in range(-3 * len(s), 3 * len(s)):
                for k in range(-len(s), len(s) + 1):
                    if k == 0:
                        self.assertRaises(ValueError, r.__getitem__,
                                          slice(i,j,k))
                    else:
                        self.assertEqual(s[i:j:k], str(r[i:j:k]))

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
