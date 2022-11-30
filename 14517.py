import sys

s = sys.stdin.readline()
n = len(s) - 1
L = []

for i in range(1, n+1):
    dp = []
    for j in range(0, n-i+1):
        if i == 1:
            p = 1
        elif i == 2:
            if s[j] == s[j+1]:
                p = 3
            else: p = 2
        else:
            p = (L[i-2][j] + L[i-2][j+1] - L[i-3][j+1]) % 10007
            if s[j] == s[j+i-1]: 
                p += L[i-3][j+1] + 1
        dp.append(p%10007)
    L.append(dp)

print(L[-1][0]%10007)
