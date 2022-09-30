import sys
list = []
a = int(sys.stdin.readline())
def checkprime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
for i in range(a):
    n = int(sys.stdin.readline())
    x = n//2
    y = n//2
    for j in range(x):
        if checkprime(x) and checkprime(y):
            print(x, y)
            break
        else:
            x -= 1
            y += 1