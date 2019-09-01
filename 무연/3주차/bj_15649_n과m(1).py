def back(choice):
    if len(choice) == m:
        print(*choice)
    else:
        for i in range(1, n + 1):
            if used[i]:
                used[i] = 0
                choice.append(i)
                back(choice)
                used[i] = 1
                choice.pop()

n, m = map(int, input().split())
used = [1] * (n + 1)
back([])