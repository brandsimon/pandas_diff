import unittest
import pandas
from pandas.testing import assert_frame_equal
from unittest.mock import MagicMock
from pandas_diff.dataframe import (compare_dataframes, convert_index_cols,
                                   built_numpy_dtypes)


class DataFrameTest(unittest.TestCase):

    def test_convert_index_cols_none(self):
        self.assertEqual(
            None,
            convert_index_cols(None))

    def test_convert_index_cols_single(self):
        self.assertEqual(
            7,
            convert_index_cols("7"))

    def test_convert_index_cols_multi(self):
        self.assertEqual(
            [3, 5, 1],
            convert_index_cols("3,5,1"))

    def test_built_numpy_dtypes(self):
        class1 = MagicMock()
        class2 = MagicMock()
        class3 = MagicMock()
        class1.__name__ = "class 1 name"
        class2.__name__ = "class 2 name"
        class3.__name__ = "class 3 name"

        sctypes = {
            'int': [class1, class2],
            'float': [class3],
        }

        self.assertEqual(
            built_numpy_dtypes(sctypes=sctypes),
            {'class 1 name': class1,
             'class 2 name': class2,
             'class 3 name': class3})

    def test_compare_dataframes_equal(self):
        data = {'left': [5, 7, 9, 11],
                'right': [6, 12, 16, 19]}
        index = [0, 1, 2, 3]
        dataframe_x = pandas.DataFrame(index=index, data=data)
        dataframe_y = pandas.DataFrame(index=index, data=data)
        assert_frame_equal(
            compare_dataframes(dataframe_x, dataframe_y),
            pandas.DataFrame())

    def test_compare_dataframes_values_differ(self):
        data_x = {'left': [5, 7, 9, 11],
                  'right': [6, 12, 16, 19]}
        data_y = {'left': [5, 8, 9, 11],
                  'right': [6, 12, 17, 19]}
        index = [0, 1, 2, 3]
        dataframe_x = pandas.DataFrame(index=index, data=data_x)
        dataframe_y = pandas.DataFrame(index=index, data=data_y)
        assert_frame_equal(
            compare_dataframes(dataframe_x, dataframe_y),
            pandas.DataFrame(
                index=pandas.MultiIndex(levels=[[0, 1, 2, 3],
                                                ['left', 'right']],
                                        codes=[[1, 2], [0, 1]]),
                data={'changed_x': [7, 16],
                      'changed_y': [8, 17]}))

    def test_compare_dataframes_indexes_differ(self):
        data = {'left': [5, 8, 9, 11],
                'right': [6, 12, 17, 19]}
        index_x = [0, 1, 3, 4]
        index_y = [0, 2, 3, 5]
        dataframe_x = pandas.DataFrame(index=index_x, data=data)
        dataframe_y = pandas.DataFrame(index=index_y, data=data)
        assert_frame_equal(
            compare_dataframes(dataframe_x, dataframe_y),
            pandas.DataFrame(
                index=[1, 3],
                data={'changed_index_x': [1, 4],
                      'changed_index_y': [2, 5]}))
