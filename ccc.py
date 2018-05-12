

# m = 3
# n = 4


color = 0

mm = {}


def update(x, y):
    updated = False
    if x > 0 and p[x - 1][y] != -1 and p[x - 1][y] < p[x][y]:
        p[x][y] = p[x - 1][y]
        updated = True
    if x < m - 1 and p[x + 1][y] != -1 and p[x + 1][y] < p[x][y]:
        p[x][y] = p[x + 1][y]
        updated = True
    if y > 0 and p[x][y - 1] != -1 and p[x][y - 1] < p[x][y]:
        p[x][y] = p[x][y - 1]
        updated = True
    if y < n - 1 and p[x][y + 1] != -1 and p[x][y + 1] < p[x][y]:
        p[x][y] = p[x][y + 1]
        updated = True

    if updated:
        if x > 0:
            update(x - 1, y)
        if x < m - 1:
            update(x + 1, y)
        if y > 0:
            update(x, y - 1)
        if y < n - 1:
            update(x, y + 1)


def add(x, y):
    global color

    if x < 0 or x >= m or y < 0 or y > n:
        return

    p[x][y] = color
    color += 1
    update(x, y)
    print getcolor(),


def printa():
    for i in range(0, m):
        for j in range(0, n):
            print str(p[i][j]) + ",",
        print ''


def getcolor():
    mm = {}
    for i in range(0, m):
        for j in range(0, n):
            if p[i][j] != -1:
                mm[p[i][j]] = 1
    return len(mm)


# add(0, 0)
#
# add(0, 1)
# add(1, 2)
# add(2, 1)


#printa()



m = int(input())
n = int(input())
k = int(input())

p = []
for i in range(0, m * 2):
    p.append([-1] * n * 2)

for i in range(0, k):
    s = raw_input()
    A = [int(aa) for aa in s.split()]
    x = int(A[0])
    y = int(A[1])
    add(x, y)
