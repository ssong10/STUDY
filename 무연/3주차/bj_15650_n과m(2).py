def back(choice, i):
    if len(choice) == m:
        print(*choice)
    else:
        for j in range(i, n + 1):
            if not used[j]:
                used[j] = 1
                choice.append(j)
                back(choice, j+1)
                used[j] = 0
                choice.pop()


n, m = map(int, input().split())
used = [0] * (n + 1)
back([], 1)