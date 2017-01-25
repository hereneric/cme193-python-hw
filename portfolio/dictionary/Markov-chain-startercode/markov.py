import random
import sys

def process_line(line):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''
    result = []
    words = line.split(" ")
    words.append('END')
    words.insert(0, 'BEGIN')
    for i in range(len(words) - 1):
        result.append((words[i], words[i + 1]))
    return result

def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    # Placeholder until we add File I/O in part two
    # Overwrite the following lines with your code:
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for line in content:
        if len(line) < 1:
            continue
        tuples = process_line(line)
        for tupl in tuples:
            if tupl[0] not in d:
                d[tupl[0]] = [tupl[1]]
            else:
                d[tupl[0]].append(tupl[1])
    return d

def generate_line(d):
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''
    string = ""
    count = 0
    cur = random.choice(d["BEGIN"])
    while cur != "END" and count < 100:
        string += " "
        string += cur
        next_list = d[cur]
        cur = random.choice(next_list)
        count += 1
    return string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'ERROR: Run as python markov.py <filename>'
        exit()

    d = process_textfile(sys.argv[1])
    print generate_line(d)
