import sys
assert(len(sys.argv) == 2)
with open(sys.argv[1], 'r') as ifile:
    lines = ifile.readlines()

def min_rgb(record):
    record = record.split(':')[1]
    hands = record.split(';')
    rgb = [0, 0, 0]
    for hand in hands:
        hand = hand.strip()
        cubesets = hand.split(',')
        for cubeset in cubesets:
            cubeset = cubeset.strip()
            cubeset = cubeset.split(' ')
            count = cubeset[0]
            count = int(count)
            colour = cubeset[1]
            match colour:
                case 'red':
                    rgb[0] = max(rgb[0], count)
                case 'green':
                    rgb[1] = max(rgb[1], count)
                case 'blue':
                    rgb[2] = max(rgb[2], count)
    return rgb

sum = 0
for i in range(len(lines)):
    rgb = min_rgb(lines[i])
    sum += rgb[0] * rgb[1] * rgb[2]

print(sum)
