import sys
n = int(sys.stdin.readline())
def getgcd(a,b):
    if a == 0 or b == 0:
        return a+b
    elif a > b:
        return getgcd(a%b, b)
    else : return getgcd(b%a, a)
L = []
for i in range(n):
    L.append(int(sys.stdin.readline()))
L.sort()

gcd = L[1] - L[0]
for i in range(2, n):
	gcd = getgcd(gcd, L[i]-L[i-1])
ans = []
for i in range(2, int(gcd**0.5)+1):
    if gcd % i == 0:
        ans.append(i)
        if i**2 != gcd:
            ans.append(gcd//i)
ans.sort()
for i in ans:
    print(i, end= " ")
print(gcd)