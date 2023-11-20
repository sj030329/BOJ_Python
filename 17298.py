# stack

n = int(input())

a = list(map(int, input().split()))

stack = []
ans = [-1] * n
for i in range(n):
    if not stack:
        stack.append([a[i], i])
    else:
        if a[i] <= stack[-1][0]:
            stack.append([a[i], i])
        else:
            while stack:
                if a[i] > stack[-1][0]:
                    t = stack.pop()
                    ans[t[1]] = a[i]
                else:
                    break
            stack.append([a[i], i])
for i in ans:
    print(i, end=" ")