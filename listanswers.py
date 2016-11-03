import os
import re

answers_regex = re.compile(r'.*answers.*')

file_list = os.listdir('.')
answers_list = []

# for file in file_list:
#     if answers_regex.search(file) is not None:
#         answers_list.append(file)

answers_list = [file for file in file_list if answers_regex.search(file) is not None]

print(answers_list)
