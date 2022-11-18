## dynamic programming

s1 = str(input())
s2 = str(input())
n1 = len(s1)
n2 = len(s2)

DP = [[0 for j in range(n1)] for i in range(n2)]

for i in range(n1):
    if s2[0] in s1[0:i+1]:
        DP[0][i] = 1

for i in range(n2):
    if s1[0] in s2[0:i+1]:
        DP[i][0] = 1

for i in range(1, n2):
    for j in range(1, n1):
        at = 0
        if s2[i] == s1[j]:
            at = 1
        DP[i][j] = max(DP[i][j-1], DP[i-1][j-1]+at, DP[i-1][j])
print(DP[-1][-1])