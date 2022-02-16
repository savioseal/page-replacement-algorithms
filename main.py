from processor import PageProcessor
from page import PageTask
import sys
import csv
import timeit

"""Script for simulating page replacement. Calculates average page faults per test, 
average page hits pet test, average page fault rate in %, and other data.

Input arguments:
input file in .csv format
number of frames to simulate physical memory

If no arguments are given, the default input and output are "input" and "results"

Output data is in .csv format"""

if __name__ == "__main__":

    if len(sys.argv) == 3:
        file = sys.argv[1]
        frame_num = int(sys.argv[2])
    else:
        file = 'input'
        frame_num = 3

    file += '.csv'

    #   Create processor for pages
    page_proc = PageProcessor()

    #   List for page arrays
    lines = []

    with open(file, 'r') as f:
        reader = csv.reader(f)
        i = 0
        for line in reader:
            tmp_line = []
            for char in line:
                tmp_line.append(PageTask(i, int(char)))
                i += 1
            lines.append(tmp_line)

    print("START")
    n = 0
    for line in lines:
        n += len(line)

    print("Total pages: " + str(n))
    print("Frames size: " + str(frame_num) + "\n")

    output_list_fifo = []
    output_list_lru = []
    list_of_outputs = []

    header1 = ["Page faults", "Page hits", "Page fault rate %"]

    #   FIFO
    starttime_fifo = timeit.default_timer()

    result_fifo = [0, 0]
    counter = 0
    for line in lines:
        result = page_proc.first_in_first_out(line, frame_num)

        for x in range(2):
            result_fifo[x] += result[x]
        av_results_fifo = [result[0], result[1]]

        output_list_fifo.append(["FIFO"])
        output_list_fifo.append(["Line " + str(counter)])
        output_list_fifo.append(header1)

        output_list_fifo.append(
            [result[0], result[1], result[0]*100/len(line)])
        counter += 1

    endtime_fifo = timeit.default_timer()

    mean_result_fifo = [result_fifo[0]/counter,
                        result_fifo[1]/counter, result_fifo[0]*100/n]

    #   Adding averages of all tests
    output_list_fifo.append([])
    output_list_fifo.append(["Average page faults per test",
                            "Average page hits per test", "Average page fault rate %"])
    output_list_fifo.append(mean_result_fifo)
    av_elapsed_time = round((endtime_fifo-starttime_fifo)/counter, 6)
    output_list_fifo.append(["Average time to process"])
    output_list_fifo.append([av_elapsed_time])

    list_of_outputs.append(output_list_fifo)

    #   LRU
    starttime_lru = timeit.default_timer()

    result_lru = [0, 0]
    counter = 0
    for line in lines:
        result2 = page_proc.least_recently_used(line, frame_num)

        for x in range(2):
            result_lru[x] += result2[x]
        av_results_lru = [result2[0], result2[1]]

        output_list_lru.append(["LRU"])
        output_list_lru.append(["Line " + str(counter)])
        output_list_lru.append(header1)

        output_list_lru.append(
            [result2[0], result2[1], result2[0]*100/len(line)])
        counter += 1

    endtime_lru = timeit.default_timer()

    mean_result_lru = [result_lru[0]/counter,
                       result_lru[1]/counter, result_lru[0]*100/n]

    #   Adding averages of all tests
    output_list_lru.append([])
    output_list_lru.append(["Average page faults per test",
                            "Average page hits per test", "Average page fault rate %"])
    output_list_lru.append(mean_result_lru)
    av_elapsed_time = round((endtime_lru-starttime_lru)/counter, 4)
    output_list_lru.append(["Average time to process"])
    output_list_lru.append([av_elapsed_time])

    list_of_outputs.append(output_list_lru)

    print("FIFO:\n" + "[Faults, Hits]: [" + str(mean_result_fifo[0]
                                                ) + ", " + str(mean_result_fifo[1]) + "]")
    print("Elapsed time: ", round(endtime_fifo - starttime_fifo, 4))
    print("\nLRU:\n" + "[Faults, Hits]: [" +
          str(mean_result_lru[0]) + ", " + str(mean_result_lru[1]) + "]")
    print("Elapsed time: ", round(endtime_lru - starttime_lru, 4))

    print("\nEND")

    #   Writing results to file

    count = 0
    for item in list_of_outputs:
        output_file = 'results' + str(count) + '.csv'
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerows(item)
        count += 1
