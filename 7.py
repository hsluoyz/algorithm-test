# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def aaa(self, s, p, i):
        if not p:
            return
        else:
            s[i] = p.val
            self.aaa(s, p.left, 2 * i + 1)
            self.aaa(s, p.right, 2 * i + 2)

    def Serialize(self, root):
        s = [-1] * 1000
        self.aaa(s, root, 0)
        end = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != -1:
                end = i
                break
        if end >= 0:
            s = s[:end + 1]
        else:
            s = []
        return s

    def Deserialize(self, s):
        if len(s) == 0:
            return None

        map = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] != -1:
                map[i] = TreeNode(s[i])
                if 2 * i + 1 < len(s) and s[2 * i + 1] != -1:
                    map[i].left = map[2 * i + 1]
                if 2 * i + 2 < len(s) and s[2 * i + 2] != -1:
                    map[i].right = map[2 * i + 2]
        return map[0]

t1 = TreeNode(8)
t2 = TreeNode(8)
t3 = TreeNode(7)
t4 = TreeNode(9)
t5 = TreeNode(2)
t6 = TreeNode(4)
t7 = TreeNode(7)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t5.left = t6
t5.right = t7

s = Solution()
d = s.Serialize(None)
print d
print s.Deserialize(d)