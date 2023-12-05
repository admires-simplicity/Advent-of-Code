import sys
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lines = list(filter(None, lines)) # contains all non-falsy (i.e. nonempty) values

def parse(s):
    sl = s[s.find(':')+1:].split('|')
    sl[0] = set(filter(None, sl[0].strip().split(' '))) # filter none to remove ''s
    sl[1] = list(filter(None, sl[1].strip().split(' ')))
    return sl

def score(card):
    return len(list(filter(lambda x : x in card[0], card[1])))

card_table = list(map(parse, lines))

counts = list(map(lambda x : 1, list(range(len(card_table)))))

for i in range(len(counts)):
    for j in range(i+1, i+1+score(card_table[i])):
        counts[j] += counts[i] # since each card i wins a card j

print(sum(counts))
