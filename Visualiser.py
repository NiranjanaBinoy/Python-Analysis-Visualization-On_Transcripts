# -*- coding: utf-8 -*-

import numpy
from matplotlib import pyplot as plt


class Visualiser:

    # constructor
    def __init__(self, data):
            self.data = data
            self.average = numpy.zeros(6)

    # method to calculate the average of statistical values from task 2
    def compute_averages(self):
        count = 0
        statement_total, vocabulary_total, repeat_total, retrace_total, error_total, pause_total = 0, 0, 0, 0, 0, 0

        #looping through numpy.array
        for arr in numpy.nditer(self.data, flags=['external_loop'], order='F'):
            temp = 0
            # finding the toal
            while temp < len(arr):
                if count == 0:
                    statement_total += arr[temp]
                elif count == 1:
                    vocabulary_total += arr[temp]
                elif count == 2:
                    repeat_total += arr[temp]
                elif count == 3:
                    retrace_total += arr[temp]
                elif count == 4:
                    error_total += arr[temp]
                elif count == 5:
                    pause_total += arr[temp]
                temp += 1
            count += 1

        # finding the number of files
        file_size = self.data.size / 6

        # finding the average
        self.average[0] = statement_total / file_size
        self.average[1] = vocabulary_total / file_size
        self.average[2] = repeat_total / file_size
        self.average[3] = retrace_total / file_size
        self.average[4] = error_total / file_size
        self.average[5] = pause_total / file_size

    # creating a bar plot using pandas plot to visualize the statistics.
    def visualise_statistics(self):
        # defining x axis
        x = ['statements', 'vocabulary', 'repeats', 'retraces', 'errors', 'pauses']
        plt.bar(x, self.average, color='b', align='center')
        plt.title('Child Language analysis')
        plt.xlabel('Characteristics')
        plt.ylabel('Statistics')
        plt.show()
