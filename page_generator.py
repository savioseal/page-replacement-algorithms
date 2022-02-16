from random import seed
from random import randint
import csv
import os
import sys

"""Small script for generating .csv files filled with data. Data is used for my other script that
simulates page replacement. Each line in file is another array of data.

Script is launched as follows:
page_generator.py filename lines_per_file values_per_line max_value seed_num

If launched without arguments, it works on default values"""

if __name__ == "__main__":

    max_arg_val = 100

    if len(sys.argv) == 6:
        filename = sys.argv[1]
        lines_per_file = min(int(sys.argv[2]), max_arg_val)
        values_per_line = min(int(sys.argv[3]), max_arg_val)
        max_value = min(int(sys.argv[4]), max_arg_val)
        seed_num = int(sys.argv[5])
    else:
        filename = 'file'
        lines_per_file = 4
        values_per_line = 10
        max_value = 20
        seed_num = 1

    text = ""

    seed(seed_num)

    #   Create files and fill them with data
    val_list = []
    file_list = []

    new_filename = filename + '.csv'

    with open(new_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for x in range(lines_per_file):
            val_list = []
            for y in range(values_per_line):
                val = randint(0, max_value)
                val_list.append(val)
            file_list.append(val_list)

        writer.writerows(file_list)
