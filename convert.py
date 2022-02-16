import csv
import sys

"""Converts input .csv file into string of values with spaces between like example below:
1 2 3 4 5 6 7 8 9 10 11 12
It was used to test algorithms on site https://nicomedes.assistedcoding.eu/#/app/os/page_replacement"""

if __name__ == "__main__":

    file = sys.argv[1]

    lines = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        i = 0
        for line in reader:
            tmp_line = []
            for char in line:
                tmp_line.append(int(char))
                i += 1
            lines.append(tmp_line)

    text = ""

    i = 0
    lines_int = []
    for line in lines:
        line_text = "Line " + str(i)
        text = ""
        for v in line:
            text += str(v) + " "
        print(line_text)
        print(text)
        print()
        i += 1
