## stack

import sys
stack = []
n = int(input())
for i in range(n):
    command = str(sys.stdin.readline()).rstrip()
    if command[0:4] == "push":
        stack.append(command[5:])
    if command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    if command == "size":
        print(len(stack))
    if command == "empty":
        if len(stack) == 0:
            print(1)
        else: print(0)
    if command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])