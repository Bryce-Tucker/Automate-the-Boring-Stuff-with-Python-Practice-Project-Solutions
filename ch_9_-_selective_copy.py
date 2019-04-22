#! pyhton3
# Selective Copy: A program to copy all files of given extension type in given file tree to given folder
# Usage: Program can be called with all three parameters, "selective_copy.py [source file tree] [file extension] [destination folder]"
#        If all paramters aren't given when the program is called, then the user will be promted through the command line to enter them individually

import os, sys, shutil

# Obtain all information required to run program
if len(sys.argv) == 4:
    src = sys.argv[1]
    ext = sys.argv[2]
    dst = sys.argv[3].strip('.')
else:
    src = input("Enter path to the source file tree: ")
    ext = input("Enter file extension of files you'd like copied: ")
    dst = input("Enter path to copy destination: ").strip('.')

# Check validity of source file tree
if os.path.isdir(src) == False:
    print("Source file tree ({}) isn't valid, make sure the path is valid and try again.".format(src))
    sys.exit()

# Check if destination directory exists, if not prompt user to confirm the creation of the new directories
if os.path.isdir(dst) == False:
    validation = ' '
    while validation != 'y' or validation != 'n':
        validation = input(" \nThe given destination directory doesn't exist. Would you like to create \"{}\"?\n\n(Y\\N)\n\n".format((dst if os.path.isabs(dst) else os.path.abspath(dst))))
        if validation.lower() == 'y':
            break
        elif validation.lower() == 'n':
            print("\n\nFile will not be created. Program quitting...")
            sys.quit()
        print("\n\nRespond with either \"Y\" for Yes or \"N\" for No")
    os.makedirs(dst)

files_to_copy = {}

# Walk through file tree and popule files_to_copy dict with all files to copy. The keys of the dicts consist of files basename, and the values consist of all paths to files with that name
for folder_name, subfolders, filenames in os.walk(src):
    for filename in filenames:
        if filename.split('.')[len(filename.split('.')) - 1] == ext:
            files_to_copy.setdefault(filename, [])
            files_to_copy[filename].append(folder_name)

# Copy files to given destination ensuring that any files with the same names are all copied without overwriting previous copies
for k,v in files_to_copy.items():
    if len(v) > 1:
        for i in range(len(v)):
            shutil.copy(os.path.join(v[i],k),os.path.join(dst, k.replace("." + str(ext), " (Occurence #{}).".format(i) + str(ext))))
    else:
        shutil.copy(os.path.join(v[0],k), os.path.join(dst,k))

print("\n\nDone copying files.")
