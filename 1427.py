a = input()
L = []
for i in range(len(a)):
    L.append(a[i])
L.sort()
L.reverse()
for i in range(len(a)):
    print(L[i], end = "")