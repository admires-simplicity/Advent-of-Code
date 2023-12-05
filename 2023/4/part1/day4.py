import sys
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = list(filter(None, lines)) # contains all non-falsy (i.e. nonempty) values

def parse(s):
    sl = s[s.find(':')+1:].split('|')
    sl[0] = set(filter(None, sl[0].strip().split(' '))) # filter none to remove ''s
    sl[1] = list(filter(None, sl[1].strip().split(' ')))
    return sl

def score(count):
    if count == 0:
        return 0
    else:
        return 2 ** (count - 1)

data = list(map(parse, lines))

win_nums = list(map(
    lambda d : 
        list(filter(
            lambda x : x in d[0],
            d[1])),
    data))

counts = list(map(len, win_nums))

scores = list(map(score, counts))

print(sum(scores))

