#! python3
# Deleting Unneeded Files: Walks through given folder tree and prints out all files larger than given threshold
# Usage: The parameters of Folder Tree and Size Threshold can be given when calling the program (in that order), or the user can respond to the command line prompts for the same information

import sys, os, math

def smallest_byte_representation(bytes):
    if bytes >= 1 * (10**9):
        return (str(round(bytes/(1 * (10**9)), 2)) + " GB")
    elif bytes >= 1 * (10**6):
        return (str(round(bytes/(1 * (10**6)), 2)) + " MB")
    elif bytes >= 1 * (10**3):
        return (str(round(bytes/(1 * (10**3)), 2)) + " KB")
    else:
        return (str(bytes) + " B")

# Get required information
if len(sys.argv) == 3:
    tree = sys.argv[1]
    size = sys.argv[2]
else:
    tree = input(" \nEnter the path to the folder tree you'd like to search: ")
    size = input("\nEnter the size throshold you'd like to use (Number followed by B, KB, MB, GB): ").lower()

# Very existence of provided tree
if os.path.isdir(tree) == False:
    print("\n\nThe given file tree doesn't exist. Verify the path and try again.")
    sys.exit()

# Verify that size input is valid, and convert it to bytes
try:
    if "gb" in size:
        size = float(size.replace("gb","")) * (10**9)
    elif "mb" in size:
        size = float(size.replace("mb","")) * (10**6)
    elif "kb" in size:
        size = float(size.replace("kb","")) * (10**3)
    else:
        size = float(size.replace("b",""))
except ValueError:
    print("\n\nThe given file size isn't valid. Verify your input follows the proper format and try again.")
    sys.exit()

large_files = {}
sizes = []
longest_line = len("Files in {} larger than {}".format(tree, smallest_byte_representation(size)))

# Walk through folder tree and  grab the paths to files larger than given threshold and their sizes.
for folder_name, subfolders, filenames in os.walk(tree):
    for filename in filenames:
        if os.path.getsize(os.path.join(folder_name, filename)) >= size:
            large_files.setdefault(os.path.getsize(os.path.join(folder_name, filename)), [])
            large_files[os.path.getsize(os.path.join(folder_name, filename))].append(os.path.join(folder_name,filename))
            if os.path.getsize(os.path.join(folder_name, filename)) not in sizes:
                sizes.append(os.path.getsize(os.path.join(folder_name, filename)))
            if len(os.path.join(folder_name,filename) + "  |  {}".format(smallest_byte_representation(os.path.getsize(os.path.join(folder_name, filename))))) > longest_line:
                longest_line = len(os.path.join(folder_name,filename) + "  |  {}".format(smallest_byte_representation(os.path.getsize(os.path.join(folder_name, filename)))))

#Print table of results
print("\n\n" + "Files in {} larger than {}".format(tree, smallest_byte_representation(size)).center(longest_line))
print("_" * (longest_line + 12))
if len(sizes) == 0:
    print("No results found")
for siz in sorted(sizes, reverse=True):
    for file in large_files[siz]:
        print(file.ljust(longest_line) + "  |  " + "{}".format(smallest_byte_representation(siz)).rjust(7))
