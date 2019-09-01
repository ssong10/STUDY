def back(choice, i):
    if len(choice) == m:
        print(*choice)
    else:
        for j in range(i, n + 1):
            choice.append(j)
            back(choice, j)
            choice.pop()

n, m = map(int, input().split())
back([], 1)