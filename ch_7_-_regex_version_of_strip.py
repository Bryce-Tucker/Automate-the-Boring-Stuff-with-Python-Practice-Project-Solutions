import re

def regex_strip(string_to_strip, strip_chars = '    '):
    strip_class = ''
    if string_to_strip == '':
        return ('')
    if strip_chars == '':
        return (string_to_strip)
    for i in range(len(strip_chars)):
        if strip_chars[i] not in strip_class:
            strip_class = strip_class + "'" + strip_chars[i] + "'"
            if i < len(strip_chars) - 1:
                strip_class = strip_class + ','
    start_regex = re.compile(r'^[{0}]*'.format(strip_class))
    end_regex = re.compile(r'[{0}]*$'.format(strip_class))
    string_to_strip = start_regex.sub('', string_to_strip)
    string_to_strip = end_regex.sub('', string_to_strip)
    return(string_to_strip)

#tests
print(regex_strip("     No 2nd argument given "))
print(regex_strip("Hello test World!","Hello, World!"))
print(regex_strip('', 'Empty first argument'))
print(regex_strip('Empty second argument', ''))
print(regex_strip('Everything is stripable', 'Everything is stripable'))
