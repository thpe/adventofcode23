
import sys
s = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    first = True
    firstc = ''
    lastc = ''
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


