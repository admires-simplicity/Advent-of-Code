import sys

if len(sys.argv) != 2:
    print('no args')
    exit(1)

with open(sys.argv[1], 'r') as infile:
    lines = infile.readlines()

def digit(s, i):
    if s[i].isdigit(): return s[i]

    digits = ['one', 'two', 'three', 'four', 'five', 'six',
              'seven', 'eight', 'nine'] # spec doesn't include 'zero'

    for j in range(len(digits)):
        if s[i : i + len(digits[j])] == digits[j]: return str(j+1) # could be return str(j) if we included zero

    return ''

total = 0
for line in lines:
    first_digit = ''
    for i in range(len(line) - 1): # -1 because skip newline (doesn't really matter here)
        d = digit(line, i)
        if d != '':
            if first_digit == '': first_digit = d
            last_digit = d
    total += int(first_digit + last_digit)

print(total)
