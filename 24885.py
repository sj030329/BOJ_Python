## implement

import sys
a, b, c = map(int, sys.stdin.readline().split())
stock = list(map(int, sys.stdin.readline().split()))
count = 0
money = b
loan = 0
def lastupper(stock):
    n = len(stock)
    max = 0
    for i in range(n):
        a = 0
        for j in range(i):
            if stock[n-j-1] > stock[i]:
                a = 1
        if a == 0:
            if max < i:
                max = i
    global k 
    k = i
    return stock[max]
last = lastupper(stock)
for i in range(k):
    if i != (a-1):
        if stock[i] < stock[i+1]:
            canmoney = (money + count*stock[i] - loan) * (c+1)
            if canmoney >= stock[i]:
                money += count*stock[i]
                count = 0
                money -= loan
                loan = money*c
                money += money*c
                count += money//stock[i]
                money -= count*stock[i]
        else: 
            money += count*stock[i]
            count = 0
if money+count*stock[i] < (money+count*stock[i]-loan) * (c+1) * stock[i+1] / stock[i]:
    canmoney = (money + count*stock[i] - loan) * (c+1)
    if canmoney >= stock[i]:
        money += count*stock[i]
        count = 0
        money -= loan
        loan = money*c
        money += money*c
        count += money//stock[i]
        money -= count*stock[i]
        money += count*stock[i+1]
print(money)