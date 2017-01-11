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
