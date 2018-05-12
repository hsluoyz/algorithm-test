# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import bisect

class KeyifyList(object):
    def __init__(self, inner, key):
        self.inner = inner
        self.key = key

    def __len__(self):
        return len(self.inner)

    def __getitem__(self, k):
        return self.key(self.inner[k])

class Solution(object):
    def insert(self, l, a):
        start = bisect.bisect_left(KeyifyList(l, lambda x: x.start), a.start) - 1
        end = bisect.bisect_right(KeyifyList(l, lambda x: x.end), a.end)

        if start >= 0:
            if l[start].end < a.start:
                start += 1
            else:
                a.start = l[start].start
        if end < len(l):
            if l[end].start > a.end:
                end -= 1
            else:
                a.end = l[end].end

        return (l[0:start] if start > 0 else []) + [a] + (l[end + 1:len(l)] if end + 1 < len(l) else [])
