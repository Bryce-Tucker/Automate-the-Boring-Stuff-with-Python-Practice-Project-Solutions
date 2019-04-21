#! python3

import os, sys, re

dir_path = input("Enter the path to the directory you'd like to search: ")
reg = input("Enter the regex you'd like to search the given directory for: ")

user_regex = re.compile(reg)

if os.path.isdir(dir_path):
    path_contents = os.listdir(dir_path)
    for file in path_contents:
        if file.split('.')[len(file.split('.')) - 1] == "txt":
            cur_file = open(os.path.join(dir_path, file))
            contents = cur_file.read()
            matches = user_regex.findall(contents)
            print(file + "\nNumber of matches = " + str(len(matches)))
            for match in matches:
                print(match)
            print()
            cur_file.close()
else:
    print("The directory provided: \"{}\" isn't valid. Check the address and try again.".format(dir_path))
    sys.exit()
