import unittest
from main import md5_crack


class TestMD5Cracker(unittest.TestCase):
    def test_1(self):
        self.assertEqual(md5_crack("827ccb0eea8a706c4c34a16891f84e7b", 5), "12345")

    def test_2(self):
        self.assertEqual(md5_crack("86aa400b65433b608a9db30070ec60cd", 5), "00078")
