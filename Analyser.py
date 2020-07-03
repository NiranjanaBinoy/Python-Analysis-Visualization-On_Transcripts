# -*- coding: utf-8 -*-


import re
import array


class Analyser:
        # constructor
        def __init__(self):
            self.statements = array.array('L', [])
            self.repeats = array.array('L', [])
            self.retraces = array.array('L', [])
            self.errors = array.array('L', [])
            self.pauses = array.array('L', [])
            self.vocabulary = array.array('L', [])

        # returns a formatted string
        def __str__(self):

            count = 0
            result = ''

            while count < len(self.statements):
                result = '\nNumber of statements     : ' + str(self.statements[count]) + \
                         '\nNumber of Unique words   : ' + str(self.vocabulary[count]) + \
                         '\nNumber of words repeated : ' + str(self.repeats[count]) + \
                         '\nNumber fo retraces       : ' + str(self.retraces[count]) + \
                         '\nNumber fo errors         : ' + str(self.errors[count]) + \
                         '\nNumber of pauses         : ' + str(self.pauses[count])

                count += 1
            return result

        # analysing the data to find the statistical values mentioned in the assignment
        def analyse_script(self, cleaned_file):

            # opening the file
            file = open(cleaned_file, "r")

            # reading the whole file to the variable
            file_data = file.readlines()

            # replacing the line breakers with empty string
            data = ' '.join(file_data).replace('\n', '').strip(' ')

            # count of repeats
            self.repeats.append(data.count('[/]'))

            # counting of retraces
            self.retraces.append(data.count('[//]'))

            # count of errors
            self.errors.append(data.count('[* m:+ed]'))

            # count of pauses
            self.pauses.append(data.count('(.)'))

            # forming a list of statements from the data
            statements = re.split(' [.|?|!]', data)
            # length of list will be the number of statements
            self.statements.append(len(statements))

            # removing all the special characters from the data
            data = data.replace('[//]', '')
            data = data.replace('[/]', '')
            data = data.replace('[*]', '')
            data = data.replace('[* m:+ed]', '')
            # converting the data to list based on whitespace
            vocabulary = data.split(' ')
            # removing the duplicate words and empty entries
            vocabulary = list(set(filter(None, vocabulary)))
            # counting the remaining number of words, which will be the number of unique words the child used.
            self.vocabulary.append(len(vocabulary))
