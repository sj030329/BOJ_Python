import sys, copy

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    c = []
    for j in range(n):
        cc = []
        input = sys.stdin.readline()
        if input[0] == "+":
            cc.append([0, int(input[2])])
        else:
            cc.append([1, int(input[2])])
        if input[4] == "+":
            cc.append([0, int(input[6])])
        else:
            cc.append([1, int(input[6])])
        c.append(cc)
    
    m = [1]

    for j in range(n):
        m2 = [0] * 7
        while m:
            k = m.pop()
            if c[j][0][0] == 0:
                m2[(k + c[j][0][1]) % 7] += 1
            else:
                m2[(k * c[j][0][1]) % 7] += 1
            if c[j][1][0] == 0:
                m2[(k + c[j][1][1]) % 7] += 1
            else:
                m2[(k * c[j][1][1]) % 7] += 1
        m = []
        for i in range(7):
            if m2[i] != 0:
                m.append(i)

    if 0 in m:
        print("LUCKY")
    else:
        print("UNLUCKY")

