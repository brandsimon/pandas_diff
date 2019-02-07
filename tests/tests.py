import unittest
from tests.pep_checker import Pep8Test
from tests.dataframe import DataFrameTest


def test_suite():
    return unittest.TestSuite([
        unittest.makeSuite(Pep8Test),
        unittest.makeSuite(DataFrameTest),
    ])
