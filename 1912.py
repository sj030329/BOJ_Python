## dynamic programming

import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
max_list = []
max_list.append(data[0])
for i in range(1, N):
    max_list.append(max(max_list[i-1]+data[i], data[i]))
print(max(max_list))