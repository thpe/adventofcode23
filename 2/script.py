import sys
import re


s = 0
ps = 0
re1 = re.compile(r'Game (\d+):(.*)')
regreen = re.compile(r'.* (\d+) green')
reblue = re.compile(r'.* (\d+) blue')
rered = re.compile(r'.* (\d+) red')
invalid = 0
with open(sys.argv[1], 'r') as f:
  for l in f:
    ok = True
    res = re1.match(l)
    substr = res.group(2).split(';')
#    print(substr)
    rgb = [0,0,0]
    for ss in substr:
        rgreen = regreen.match(ss)
        if rgreen is not None:
            rgreen = int(rgreen.group(1))
            rgb[1] = max(rgb[1], rgreen)
        else:
            rgreen = 0
        rblue = reblue.match(ss)
        if rblue is not None:
            rblue = int(rblue.group(1))
            rgb[2] = max(rgb[2], rblue)
        else:
            rblue = 0
        rred = rered.match(ss)
        if rred is not None:
            rred = int(rred.group(1))
            rgb[0] = max(rgb[0], rred)
        else:
            rred = 0
        if rgreen > 13 or rred > 12 or rblue > 14:
            print('invalid')
            ok = False
    if ok:
        print(substr)
        s += int(res.group(1))
    else:
        invalid += 1
    ps += rgb[0] * rgb[1] * rgb[2]

print(s)
print(invalid)

print(ps)
