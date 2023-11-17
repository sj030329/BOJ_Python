# greedy
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
cnt = [[0] for _ in range(10)]
z = []
ans = 0

for i in range(10):
    cnt[i].append(alphabet[i])

n = int(input())

for i in range(n):
    s = input()
    for j in range(len(s)-1, -1, -1):
        for k in range(10):
            if s[j] == alphabet[k]:
                cnt[k][0] += 10 ** (len(s)-j-1)
    if s[0] not in z:
        z.append(s[0])
cnt.sort(reverse=True)

for i in range(10):
    if cnt[9-i][1] not in z:
        cnt.remove(cnt[9-i])
        break

for i in range(9, 0, -1):
    ans += cnt[9-i][0] * i
    
print(ans)
     
