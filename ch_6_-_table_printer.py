def printTable(array):
    col_widths = [0] * len(array)
    for i in range(len(array[0])):
        for j in range(len(array)):
            if len(array[j][i]) > col_widths[j]:
                col_widths[j] = len(array[j][i])
    for i in range(len(array[0])):
        line = ''
        for j in range(len(array)):
            line = line + array[j][i].rjust(col_widths[j]) + " "
        print(line.rstrip())

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
