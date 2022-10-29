import sys
word = sys.stdin.readline().rstrip()
count = 0
n = len(word)
list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in range(n):
    if word[i:i+2] in list or word[i:i+3] in list:
        count += 1
print(n - count)