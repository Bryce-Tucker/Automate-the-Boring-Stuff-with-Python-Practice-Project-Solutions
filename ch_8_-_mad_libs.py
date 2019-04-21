import re, sys, os

mad_lib_regex = re.compile(r'''ADJECTIVE|NOUN|ADVERB|VERB''')

file_location = input("Enter the path to your Mad Libs text file: ")
if os.path.isfile(file_location):
    lib_file = open(file_location)
else:
    print("Failed trying to open {}, ensure that your spelling is correct, and that if the file is in another folder you are providing a full directory.".format(file_location))
    sys.exit()
mad_lib = lib_file.read()
words = mad_lib_regex.findall(mad_lib)
for word in words:
    replacement = input("Enter a {}: ".format(word.lower()))
    mad_lib = mad_lib_regex.sub(replacement, mad_lib, 1)
print(mad_lib)
lib_file.close()
