
def get(a):
    ji = 0
    ou = 0
    fo = 0
    for i in a:
        if i % 2 == 1:
            ji += 1
        elif i % 4 == 2:
            ou += 1
        else:
            fo += 1
    #print ji, ou, fo

    jiu = 0
    jiu += ji * 2
    if ou != 0:
        jiu += 2
    jiu -= 2
    #print fo - jiu / 2
    if fo - jiu / 2 >= 0:
        return "Yes"
    else:
        return "No"


# get([1, 2, 3, 4, 5, 8])

t = input()
for tt in range(t):
    x = input()
    s = raw_input()
    A = [int(n) for n in s.split()]
    print get(A)


