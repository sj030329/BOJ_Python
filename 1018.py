## brute force

import sys
n, m = map(int, sys.stdin.readline().split())
board = []
count = []
for i in range(n):
    board.append(input())
for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 1:
                    if board[k][l] != "W":
                        count1 += 1
                else:
                    if board[k][l] != "B":
                        count1 += 1
        count.append(count1)
for i in range(n-7):
    for j in range(m-7):
        count2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 1:
                    if board[k][l] != "B":
                        count2 += 1
                else:
                    if board[k][l] != "W":
                        count2 += 1
        count.append(count2)

print(min(count))