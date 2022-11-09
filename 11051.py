import sys
a,b = map(int, sys.stdin.readline().split())
def factorial(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
ans = (factorial(a) // (factorial(b)*factorial(a-b)))
print(ans%10007)