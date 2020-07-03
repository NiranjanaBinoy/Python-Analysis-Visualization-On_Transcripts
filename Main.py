# -*- coding: utf-8 -*-

import os
import numpy
import errno

from task2_StudentID import Analyser
from task3_StudentID import Visualiser

# defining the file paths to input and output file
SLI_file_path = "./SLI"
TD_file_path = "./TD"
SLI_cleaned_path = "./SLI_cleaned"
TD_cleaned_path = "./TD_cleaned"


# Methos accepts the file reader for input and output file and filter it as mentioned in the assignmeent
def pre_processing(file, output):

    output_txt = ''

    # Reading through each line on the file
    for each in file:

        # checking for the child's dialogue
        if '*CHI:' in each:

            # splitting the line to remove the *CHI: tag
            line_1 = each.split('*CHI:')[1]

            # stripping line break and tab from the line
            line = line_1.strip('\n').strip('\t')

            # splitting the line at the whitespaces to form a list
            word_list = line.split(' ')

            count = 0

            # looping through each word in the list
            while count < len(word_list):
                # storing the corresponding word to a variable after leading or trailing spaces
                word = word_list[count].strip()
                count += 1

                # checking for square brackets in the word
                if '[' in word:
                    # skipping repeating and retracing symbol
                    if word != '[//]' and word != '[/]':
                        word = ''
                elif ']' in word:
                    # checking for [* m+ed] which denotes the grammatical error, space between * and m splits the
                    # word to two
                    if word == 'm:+ed]':
                        word = '[* m:+ed]'
                    else:
                        word = ''

                # checking for words with ( or ) except (.)
                if'(' in word:
                    # checking for pauses
                    if word != '(.)':
                        word = word.replace('(', '')
                        word = word.replace(')', '')
                elif ')' in word:
                    word = word.replace(')', '')

                # checking all the non empty words prefixed with & or +
                if word != '' and (word[0] == '&' or word[0] == '+'):
                    word = ''
                
                # checking for angle brackets
                if '<' in word:
                    word = word.replace('<', '')
                if '>' in word:
                    word = word.replace('>', '')
                # if the word is not empty it is appended to the string variable
                if word != '':
                    output_txt += ' '+word

            output_txt += '\n'
            # writing the resulting ine to the designated output file
    output.write(output_txt[:-2])


print('Starting SLI files processing !!!')
# task 2 class initialization
analyser_sli = Analyser()

# looping through each file in the SLI folder
for file_name in os.listdir(SLI_file_path):

    # creating the full file paths for inout and output files in the SLI folder
    text = os.path.join(SLI_file_path, file_name)
    output = os.path.join(SLI_cleaned_path, file_name)

    # creating the output folder if it does not exist
    if not os.path.exists(os.path.dirname(output)):
        try:
            os.makedirs(os.path.dirname(output))
        except OSError as e:  # Guard against race condition
            if errno.errno != e.EEXIST:
                raise

    # opening the files
    file = open(text, 'r')
    output_file = open(output, 'w+')

    # calling the pre_processing method
    pre_processing(file, output_file)

    # closing the readers
    file.close()
    output_file.close()

    # calling the analyser
    analyser_sli.analyse_script(output)

# forming a numpy input array for task 3
sli_statistics = numpy.array([analyser_sli.statements.tolist(),
                             analyser_sli.vocabulary.tolist(),
                             analyser_sli.repeats.tolist(),
                             analyser_sli.retraces.tolist(),
                             analyser_sli.errors.tolist(),
                             analyser_sli.pauses.tolist()])

# initializing the Visualizer of task 3
visualize_sli = Visualiser(sli_statistics)

# calculating the average value of the statistics
visualize_sli.compute_averages()

# visualizing the average values in  bar chart
visualize_sli.visualise_statistics()

print('Finished processing SLI files')

print('Starting TD files processing !!!')
# task 2 class initialization
analyser_td = Analyser()

# looping through each file in the TD folder
for file_name in os.listdir(TD_file_path):

    # creating the full file paths for inout and output files in the TD folder
    text = os.path.join(TD_file_path, file_name)
    output = os.path.join(TD_cleaned_path, file_name)

    # creating the output folder if it does not exist
    if not os.path.exists(os.path.dirname(output)):
        try:
            os.makedirs(os.path.dirname(output))
        except OSError as e:  # Guard against race condition
            if errno.errno != e.EEXIST:
                raise

    # opening the files
    file = open(text, 'r')
    output_file = open(output, 'w+')

    # calling the pre_processing method
    pre_processing(file, output_file)

    # closing the readers
    file.close()
    output_file.close()

    # calling the analyser
    analyser_td.analyse_script(output)

# forming a numpy input array for task 3
td_statistics = numpy.array([analyser_td.statements.tolist(),
                            analyser_td.vocabulary.tolist(),
                            analyser_td.repeats.tolist(),
                            analyser_td.retraces.tolist(),
                            analyser_td.errors.tolist(),
                            analyser_td.pauses.tolist()])

# initializing the Visualizer of task 3
visualize_td = Visualiser(td_statistics)

# calculating the average value of the statistics
visualize_td.compute_averages()

# visualizing the average values in  bar chart
visualize_td.visualise_statistics()
print('Finished processing TD files')
