# Complete the function below.

import sys

sys.stdout.softspace=0

def  socialGraphs(counts):
    m = {}
    for i in range(0, len(counts)):
        if not m.has_key(counts[i]):
            m[counts[i]] = []
            m[counts[i]].append(i)
        else:
            m[counts[i]].append(i)
    #print m

    l = []
    for k, v in m.items():
        for i in range(0, len(v), k):
            l.append(v[i:(i + k)])
    #print l

    l.sort(key=lambda a: a[0])

    for item in l:
        for i in range(0, len(item)):
            if i != len(item) - 1:
                sys.stdout.write(str(item[i]) + ' ')
            else:
                sys.stdout.write(str(item[i]))
        print ''



socialGraphs([2, 2, 2, 2])
socialGraphs([1, 1, 1])
socialGraphs([2, 1, 1, 2, 1])
