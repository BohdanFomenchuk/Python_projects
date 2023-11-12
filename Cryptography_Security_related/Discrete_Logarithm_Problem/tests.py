import unittest
from main import crack


class DiscreteLog(unittest.TestCase):
    def test_crack_1(self):
        self.assertEqual(crack(654, 4547, 11087), 114)

    def test_crack_2(self):
        self.assertEqual(crack(253941, 1587010, 2450219), 15331)

    def test_crack_3(self):
        self.assertEqual(crack(59930016, 465179611, 618142807), 36249002)

    def test_crack_4(self):
        self.assertEqual(crack(303566540, 5272582361, 11123061581), 100529399)

    def test_crack_5(self):
        self.assertEqual(crack(49999999961, 42, 49999999967), 23150749045)
