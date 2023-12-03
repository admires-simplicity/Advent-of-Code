import sys
with open(sys.argv[1], 'r') as file:
#with open('in1', 'r') as file:
    lines = file.readlines()

#symbols = []
#for i in range(len(lines)):
#    for j in range(len(lines[i])):
#        if not (lines[i][j] == '.' or lines[i][j].isalpha() or lines[i][j].isdigit() or lines[i][j] == '\n'):
#            symbols = symbols + [(i, j)]

def symbol(c):
    return not (c == '.' or c.isdigit() or c == '\n')

def adjacent_symbol(i, j):
    if i > 0:
        if j > 0 and symbol(lines[i-1][j-1]): return True
        if symbol(lines[i-1][j]): return True
        if j < len(lines[i]) - 1 and symbol(lines[i-1][j+1]): return True

    if j > 0 and symbol(lines[i][j-1]): return True
    if j < len(lines[i]) - 1 and symbol(lines[i][j+1]): return True

    if i < len(lines) - 1:
        if j > 0 and symbol(lines[i+1][j-1]): return True
        if symbol(lines[i+1][j]): return True
        if j < len(lines[i]) - 1 and symbol(lines[i+1][j+1]): return True


total = 0
current_digits = []
found_symbol = False
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            current_digits += [lines[i][j]]
            if not found_symbol:
                found_symbol = adjacent_symbol(i, j)
        else:
            if current_digits and found_symbol:
                total += int(''.join(map(str, current_digits)))
            current_digits = []
            found_symbol = False

print(total)

