## math

import sys
exp = sys.stdin.readline().split('-')
sum = 0
for i in exp[0].split('+'):
    sum += int(i)
for i in exp[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)