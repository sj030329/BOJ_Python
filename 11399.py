## greedy

a = int(input())
b = list(map(int, input().split()))
count = 0
b.sort()
for i in range(a):
    count += b[i] * (a-i)

print(count)