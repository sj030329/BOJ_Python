import sys
s = sys.stdin.readline().rstrip()
while s != ".":
    check = 0
    bracket = []
    for i in s:
        if i == "(":
            bracket.append(i)
        if i == ")":
            if len(bracket) == 0:
                check = -1
            elif bracket[-1] == "[":
                check = -1
            else : bracket.pop()
        if i == "[":
            bracket.append(i)
        if i == "]":
            if len(bracket) == 0:
                check = -1
            elif bracket[-1] == "(":
                check = -1
            else : bracket.pop()
    if len(bracket) != 0:
        check = -1
    if check == 0:
        print("yes")
    else: print("no")
    s = sys.stdin.readline().rstrip()