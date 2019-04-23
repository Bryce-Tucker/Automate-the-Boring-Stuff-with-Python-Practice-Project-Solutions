#! python3

# Filling in the Gaps: A program that will rename numbered files to ensure that there are no gaps between the file's numbers

import sys, os, re, shutil

if len(sys.argv) == 3:
    folder = sys.argv[1]
    prefix = sys.argv[2]
else:
    folder = input("Enter the directory path: ")
    prefix = input("Enter file prefix: ")

if os.path.isdir(folder) == False:
    print("Given directory doesn't exist. Vefiry the path given and try again.")
    sys.exit()

file_regex = re.compile(r'''(({})(\s*)(\d+))'''.format(prefix))

'''print(os.listdir(folder))
print("\n\n")
print(str(os.listdir(folder)))
print("\n\n")
import pprint
print(file_regex.findall(str(os.listdir(folder))))

print("\n\n")'''

matches = []
for file in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, file)) and file_regex.search(file) != None:
        matches.append(file)
mathches = sorted(matches)
#tmp = file_regex.search(matches[0]).groups()[len(file_regex.search(matches[0]).groups()) - 1]
num_width = len(file_regex.search(matches[0]).groups()[len(file_regex.search(matches[0]).groups()) - 1])
if len(file_regex.search(matches[(len(matches) - 1)]).groups()[len(file_regex.search(matches[(len(matches) - 1)]).groups()) - 1]) > num_width:
    num_width = len(file_regex.search(matches[(len(matches) - 1)]).groups()[len(file_regex.search(matches[(len(matches) - 1)]).groups()) - 1])

print(num_width)
prompt = "1"
if int(file_regex.search(matches[0]).groups()[len(file_regex.search(matches[0]).groups()) - 1]) > 1:
    print("\n\nThe files starting with the prefix \"{}\" don't start at 1, would you like keep the starting number of {} or start at 1?".format(prefix, int(file_regex.search(matches[0]).groups()[len(file_regex.search(matches[0]).groups()) - 1])))
    prompt = input("(1) Start at 1\n(2) Keep current starting point\n")
    while prompt != '1' and prompt != '2':
        prompt = input("Respond with either 1 or 2 to make a selections, or respond with Q to quit.\n")
        if prompt.lower() == 'q':
            sys.exit()

mod = 1 if prompt == '1' else int(file_regex.search(matches[0]).groups()[len(file_regex.search(matches[0]).groups()) - 1])

for i in range(len(matches)):
    shutil.move(os.path.join(folder, matches[i]), os.path.join(folder, prefix + file_regex.search(matches[i]).groups()[2] + ('0' * (num_width - (len(str(i + mod))))) + str(i + mod)))
