## math

import sys
a = int(sys.stdin.readline())
def factorial(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    case = (factorial(c) // (factorial(b)*factorial(c-b)))
    print(case)