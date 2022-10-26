import sys
a,b = map(int, sys.stdin.readline().split())
def count5(n):
    count = 0
    while n != 0:
        n = n // 5
        count += n
    return count
def count2(n):
    count = 0
    while n != 0:
        n = n // 2
        count += n
    return count
if b == 0:
    print(0)
else:
    print(min(count2(a)-count2(b)-count2(a-b),
              count5(a)-count5(b)-count5(a-b)))