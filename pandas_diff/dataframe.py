import pandas
import numpy
import argparse


def compare_dataframes(dataframe_x, dataframe_y):
    index_differences = dataframe_x.index != dataframe_y.index
    if index_differences.any():
        index_diff_locations = numpy.where(index_differences)
        changed_index_x = dataframe_x.index[index_diff_locations]
        changed_index_y = dataframe_y.index[index_diff_locations]
        return pandas.DataFrame({'changed_index_x': changed_index_x,
                                 'changed_index_y': changed_index_y,
                                 }, index=index_diff_locations[0])
    differences = dataframe_x != dataframe_y
    if not differences.values.any():
        return pandas.DataFrame()
    differences_stacked = differences.stack()
    changed = differences_stacked[differences_stacked]
    location_differ = numpy.where(differences)
    changed_x = dataframe_x.values[location_differ]
    changed_y = dataframe_y.values[location_differ]
    return pandas.DataFrame({'changed_x': changed_x,
                             'changed_y': changed_y,
                             }, index=changed.index)


def convert_index_cols(arg):
    if arg is not None:
        if ',' in arg:
            return [int(i) for i in arg.split(',')]
        else:
            return int(arg)
    else:
        return None


def built_numpy_dtypes(sctypes):
    result = {}
    for base in sctypes:
        for dtype in sctypes[base]:
            result[dtype.__name__] = dtype
    return result


def main():
    dtypes = built_numpy_dtypes(numpy.sctypes)
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--dtype', default='object',
                           choices=dtypes.keys(),
                           help='numpy dtype')
    argparser.add_argument('--decimals', default=None,
                           help='Round both dataframes to n precision')
    argparser.add_argument('--index-col', default=None,
                           help='Use column(s) as index column\n'
                                'Example: "1", "1,3"')
    argparser.add_argument('--parse-dates', default=False,
                           action='store_true',
                           help='Parse dates')
    argparser.add_argument('--delimiter', default=',',
                           help='Delimiter in both files')
    argparser.add_argument('--outfile', default=None,
                           help='Save output to file instead of printing it')
    argparser.add_argument('file1')
    argparser.add_argument('file2')
    args = argparser.parse_args()

    index_col = convert_index_cols(args.index_col)

    def readfile(filename):
        dataframe = pandas.read_csv(
            filename,
            index_col=index_col,
            parse_dates=args.parse_dates,
            delimiter=args.delimiter,
            dtype=dtypes[args.dtype])
        if args.decimals is not None:
            dataframe = dataframe.round(int(args.decimals))
        return dataframe

    dataframe_x = readfile(args.file1)
    dataframe_y = readfile(args.file2)
    result = compare_dataframes(dataframe_x, dataframe_y)
    if args.outfile is not None:
        result.to_csv(args.outfile)
    else:
        print(result)


if __name__ == "__main__":
    main()
