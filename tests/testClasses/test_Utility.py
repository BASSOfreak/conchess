import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from src.utility.utility import letterToFile

class test_Utility(unittest.TestCase):
    def testLetterToFile(self):
        self.assertEqual(letterToFile("A"), 1)
        self.assertEqual(letterToFile("H"), 8)