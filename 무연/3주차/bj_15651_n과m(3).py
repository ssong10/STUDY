def back(choice):
    if len(choice) == m:
        print(*choice)
    else:
        for i in range(1, n + 1):
            choice.append(i)
            back(choice)
            choice.pop()


n, m = map(int, input().split())
back([])