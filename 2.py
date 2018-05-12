
import sys
import bisect


def bisearch(a, v):
    return bisect.bisect_left(a, v)


def aaa(a):
    if len(a) == 0:
        print 0
        return

    a.sort()
    res = 0
    n = len(a)
    b = []

    # for ii in range(0, n):
    #     b.append(a[ii] + 180.0)
    #
    # for i in range(0, n):
    #     for j in range(i + 1, n):
    #         s1 = a[j] - b[i]
    #         for k in range(j + 1, n):
    #             s2 = a[k] - b[i]
    #             if s1 > 0 and s2 > 0 or s1 < 0 and s2 < 0:
    #                 res += 1

    for i in range(0, n):
        flag = a[i] + 180.0
        small = bisect.bisect_left(a[i + 1:], flag)
        big = n - i - 1 - bisect.bisect_right(a[i + 1:], flag)
        #print big, small

        res += big * (big - 1) / 2
        res += small * (small - 1) / 2

        # small = 0
        # big = 0

        # for j in range(i + 1, n):
        #     if a[j] < flag:
        #         small += 1
        #     if a[j] > flag:
        #         big += 1
        # #print small, big
        # res += small * (small - 1) / 2
        # res += big * (big - 1) / 2

    print res

#aaa([0, 179, 56, 180])

a = [0, 1, 1, 1.1, 2]
small = bisect.bisect_left(a, 1)
big = len(a) - bisect.bisect_right(a, 1)
print small, big

# count = int(sys.stdin.readline()[:-1])
# a = []
# for i in range(0, count):
#     s = float(sys.stdin.readline()[:-1])
#     a.append(s)
#
# aaa(a)
