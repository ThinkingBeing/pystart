"""test for main"""
import unittest
from main import main

class TestMain(unittest.TestCase):
    """test main"""

    def test_whomai(self):
        """check my name"""
        my_name = main.whoami()
        self.assertEqual("ligf2", my_name)

    def test_whoami_include(self):
        """check name must include ligf"""
        my_name = main.whoami()
        self.assertIn("ligf", my_name)

