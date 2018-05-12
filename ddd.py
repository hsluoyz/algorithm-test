

while True:
    try:
        s = raw_input()
        A = [float(aa) for aa in s.split()]

        R = A[0]
        n = A[1]
        print pow(R, n)
    except:
        break




