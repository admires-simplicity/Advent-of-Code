import sys
assert(len(sys.argv) == 2)
with open(sys.argv[1], 'r') as ifile:
    lines = ifile.readlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def possible(record):
    record = record.split(':')[1]
    hands = record.split(';')
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
                    if count > MAX_RED: return False
                case 'green':
                    if count > MAX_GREEN: return False
                case 'blue':
                    if count > MAX_BLUE: return False
    return True

sum = 0
for i in range(len(lines)):
    if possible(lines[i]):
        sum += i+1

print(sum)
