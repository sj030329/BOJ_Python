N, K = map(int, input().split())
data = list(map(int, input().split()))
temp = 0
for i in range(K):
    temp += data[i]
max = temp
for i in range(0, N-K):
    temp -= data[i]
    temp += data[i+K]
    if max < temp:
        max = temp
print(max)