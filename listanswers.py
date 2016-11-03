import os
import re
import sys


grep_txt = sys.argv[1]

txt_regex = re.compile(r'.*.txt')
grep_regex = re.compile(sys.argv[1])

file_list = os.listdir('.')

# Create list of all files in current directory that end in '.txt'
# answers_list = []
# for file in file_list:
#     if answers_regex.search(file) is not None:
#         answers_list.append(file)

# Create list of all files in current directory that end in '.txt' - LIST COMPREHENSION VERSION
txt_list = [file for file in file_list if txt_regex.search(file) is not None]

# Iterate over each file via readlines and track line numbers
for txt in txt_list:
    print ('---------')
    parse_txt = open(txt)
    print('Grepping file ' + txt)
    linecount = 0
    found = None
    # Search for the expression and print if found
    for line in parse_txt.readlines():
        matching = grep_regex.findall(line)
        linecount += 1
        if len(matching) is not 0:
            print('Line found containing "' + grep_txt + '" at line ' + str(linecount) + ': ' + matching[0])
            found = True
    if found == None:
        print ('No Lines found containing "' + grep_txt)


