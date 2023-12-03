import sys
with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

def gear(c):
    return c == '*'

def adjacent_gear(i, j):
    if i > 0:
        if j > 0 and gear(lines[i-1][j-1]): return (i-1, j-1)
        if gear(lines[i-1][j]): return (i-1, j)
        if j < len(lines[i]) - 1 and gear(lines[i-1][j+1]): return (i-1, j+1)

    if j > 0 and gear(lines[i][j-1]): return (i, j-1)
    if j < len(lines[i]) - 1 and gear(lines[i][j+1]): return (i, j+1)

    if i < len(lines) - 1:
        if j > 0 and gear(lines[i+1][j-1]): return (i+1, j-1)
        if gear(lines[i+1][j]): return (i+1, j)
        if j < len(lines[i]) - 1 and gear(lines[i+1][j+1]): return (i+1, j+1)

    return ()


current_digits = []
current_gears = set([])
gear_dict = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            # if i,j is digit, add and check for adj gear position.
            # if adjacent gear exists, add its position to current_gears (set).
            current_digits += [lines[i][j]]
            g = adjacent_gear(i, j)
            if g:
                current_gears |= {g}
        else:
            # i,j is not a digit. if we found a digit and gear(s), for all
            # found gears, add digit to list of numbers adjacent to gear in
            # dict and reset accumulators.
            if current_digits and current_gears:
                value = int(''.join(map(str, current_digits)))
                for g in current_gears:
                    if g in gear_dict:
                        gear_dict[g] += [value]
                    else:
                        gear_dict[g] = [value]
            current_digits = []
            current_gears = set([])

total = 0
for nums in gear_dict.values():
    if len(nums) == 2:
        total += nums[0] * nums[1]

print(total)

