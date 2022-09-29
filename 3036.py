import sys
n = int(sys.stdin.readline())
def gcd(a,b):
    if a == 0 or b == 0:
        return a+b
    elif a > b:
        return gcd(a%b, b)
    else : return gcd(b%a, a)
L = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    x = gcd(L[0], L[i])
    print(int(L[0] / x), end = "")
    print("/", end="")
    print(int(L[i] / x))