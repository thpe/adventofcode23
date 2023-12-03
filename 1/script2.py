import sys
s = 0

trans = [
['one', 'one1one'],
['two', 'two2two'],
['three', 'three3three'],
['four', 'four4four'],
['five', 'five5five'],
['six', 'six6six'],
['seven', 'seven7seven'],
['eight', 'eight8eight'],
['nine', 'nine9nine']
]

with open(sys.argv[1], 'r') as f:
  for l in f:
    first = True
    firstc = ''
    lastc = ''
    for i in range(len(trans)):
        l = l.replace(trans[i][0], trans[i][1])

    print(l)
    for c in l:
        if c.isdigit():
            if first:
                firstc = c
                lastc = c
                first = False
            else:
                lastc = c
    s+=int(firstc+lastc)
print(s)


