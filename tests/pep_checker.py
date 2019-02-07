import unittest
import pycodestyle
from pyflakes.api import checkRecursive
from pyflakes import reporter

CHECK_DIRECTORYS = ["pandas_diff/", "tests/", "setup.py"]


class Pep8Test(unittest.TestCase):

    def test_pep8(self):
        style = pycodestyle.StyleGuide()
        check = style.check_files(CHECK_DIRECTORYS)
        self.assertEqual(check.total_errors, 0,
                         'PEP8 errors: %d' % check.total_errors)

    def test_pyflakes(self):
        rep = reporter._makeDefaultReporter()
        error_count = checkRecursive(CHECK_DIRECTORYS, rep)
        self.assertEqual(error_count, 0,
                         'PyFlakes errors: %d' % error_count)
