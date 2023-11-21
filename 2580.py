import sys

sudoku = []
num = 0
to_find = []

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            num += 1
            to_find.append([i, j])

def valid_num(n, k):

    x = to_find[n][0]
    y = to_find[n][1]
    x2 = x - (x % 3)
    y2 = y - (y % 3)

    for i in range(9):
        if sudoku[x][i] == k:
            return False
        if sudoku[i][y] == k:
            return False
        
    for i in range(3):
        for j in range(3):
            if sudoku[x2+i][y2+j] == k:
                return False
    return True

def complete_sudoku(n):
    if n == num:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end= " ")
            print()
        exit()

    for i in range(1, 10):
        if valid_num(n, i):
            sudoku[to_find[n][0]][to_find[n][1]] = i
            complete_sudoku(n+1)
            sudoku[to_find[n][0]][to_find[n][1]] = 0

complete_sudoku(0)