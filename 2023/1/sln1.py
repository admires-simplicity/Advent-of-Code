with open('input', 'r') as infile:
    lines = infile.readlines()

total = 0
for line in lines:
    first_digit = ''
    for char in line:
        if char.isdigit():
            if first_digit == '': first_digit = char
            last_digit = char
    total += int(first_digit + last_digit)

print(total)
