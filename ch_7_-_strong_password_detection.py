import pyperclip
import re

def strong_password_detection(password):
    at_least_eight_regex = re.compile(r'.{8}')
    has_all_chars_regex = re.compile(r'''
    [A-Z].*[a-z].*[0-9]|
    [a-z].*[A-Z].*[0-9]|
    [A-Z].*[0-9].*[a-z]|
    [a-z].*[0-9].*[A-Z]|
    [0-9].*[A-Z].*[a-z]|
    [0-9].*[a-z].*[A-Z]
    ''', re.VERBOSE)

    if at_least_eight_regex.search(password) != None and has_all_chars_regex.search(password) != None:
        print ("Password is strong")
    elif at_least_eight_regex.search(password) != None and has_all_chars_regex.search(password) == None:
        print("Password is weak: Doesn't contain at least one uppercase character, lowercase character, and digit")
    elif at_least_eight_regex.search(password) == None and has_all_chars_regex.search(password) != None:
        print("Password is weak: Isn't at least 8 charcters long")
    else:
        print("Password is weak: Isn't at least 8 charcters long and doesn't contain at least one uppercase character, lowercase character, and digit")

#tests
strong_password_detection("Test1234")
strong_password_detection("te1234ST")
strong_password_detection("test1234")
strong_password_detection("testtest")
strong_password_detection("Test123")
