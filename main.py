# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import pandas as pd
from collections import defaultdict


def main(argv):
    chunk_size = 10 ** 3
    dictionary = defaultdict(int)
    for chunk in pd.read_csv(argv[0], chunksize=chunk_size, header=None):
        last_key = process(chunk, argv[2], dictionary)
        if len(dictionary) > 1:
            temp_dict_val = dictionary.pop(last_key)
            statistics = pd.DataFrame.from_dict(dictionary, orient='index', columns=['count'])
            statistics.to_csv(argv[1], mode='a', header=False)
            dictionary = defaultdict(int)
            dictionary[last_key] = temp_dict_val
    statistics = pd.DataFrame.from_dict(dictionary, orient='index', columns=['count'])
    statistics.to_csv(argv[1], mode='a', header=False)


def process(chunk, col, dictionary):
    timestamp_col = chunk[int(col)].to_numpy()
    key = get_key(timestamp_col[0])
    if key == get_key(timestamp_col[-1]):
        dictionary[key] += len(timestamp_col)
    else:
        for timestamp in timestamp_col:
            key = get_key(timestamp)
            dictionary[key] += 1
    return key


def get_key(timestamp):
    dt_object = pd.to_datetime(timestamp, unit='ms').to_pydatetime()
    return dt_object.strftime("%b-%d-%Y %H:00")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv[1:])
