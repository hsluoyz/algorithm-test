# -*- coding:utf-8 -*-
class Solution:
    def aaa(self, a, start, end):
        if end - start == 1:
            return a[start + 1]

        mid = (start + end) / 2
        if a[start] <= a[mid]:
            return self.aaa(a, mid, end)
        else:
            return self.aaa(a, start, mid)

    def minNumberInRotateArray(self, rotateArray):
        return self.aaa(rotateArray, 0, len(rotateArray))
