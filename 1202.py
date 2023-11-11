import sys, heapq

n, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
b = [int(sys.stdin.readline()) for i in range(k)]
q0 = []
q1 = []
q2 = []
cnt = 0

for i in a:
    heapq.heappush(q0, (i[0], i[1]))
for i in b:
    heapq.heappush(q2, i)

while q2:
    t2 = heapq.heappop(q2)
    while q0:
        if q0[0][0] <= t2:
            t = heapq.heappop(q0)
            heapq.heappush(q1, (-t[1]))
        else:
            break
    if q1:
        cnt += -(heapq.heappop(q1))
print(cnt)