pp = []

# n = 5
# L = 2
# path = [0, 1, 2, 3]

n = 20
L = 4
path = [0, 0, 1, 2, 3, 2, 3, 1, 3, 0, 1, 8, 6, 8, 0, 5, 15, 0, 9]

def youli(start, end, step):
    if step <= 0 and start != end:
        return []
    if step <= 0 and start == end:
        return [start]

    if cache[start][end][step] != -1:
        return cache[start][end][step]

    b = []
    for i in range(n):
        if i != start and pp[i][start]:
            b.append(i)

    max_res = []
    for i in b:
        subres = youli(i, end, step - 1)
        if start not in subres:
            subres.append(start)
        if len(subres) > len(max_res):
            max_res = subres

    print start, end, step, max_res
    cache[start][end][step] = max_res
    return max_res


def wawa(n, L, path):
    global pp
    pp = [([0] * n) for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i != 0 and path[i - 1] == j:
                pp[i][j] = 1
                continue
            if j != 0 and path[j - 1] == i:
                pp[i][j] = 1

    print pp

    max = 0
    for i in range(1, n):
        res = youli(0, i, L)
        if max < len(res):
            max = len(res)
    print max


# s = raw_input()
# A = [int(aaa) for aaa in s.split()]
# n = A[0]
# L = A[1]
# s = raw_input()
# path = [int(aaa) for aaa in s.split()]

cache = []
for i in range(0, n):
    cc = []
    for j in range(0, n):
        cc.append([-1] * (L + 1))
    cache.append(cc)



wawa(n, L, path)
