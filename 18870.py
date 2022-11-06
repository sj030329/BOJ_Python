import sys

a = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split()))]
L = list(sorted(set(data[0])))
data2 = {L[i]:i for i in range((len(L)))}
for i in data[0]:
    print(data2[i], end = " ")