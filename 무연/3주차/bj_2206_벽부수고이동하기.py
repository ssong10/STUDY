def dfs(i, j, count, p):
    global answer
    if (i, j) == (n, m):
        answer = count
        return
    visit[i][j] = 1
    for k in range(4):
        if 0 <= i + x[k] < n and 0 <= j + y[k] < m:
            if not miro[i + x[k]][j + y[k]]:
                if not visit[i + x[k]][j + y[k]]:
                    visit[i + x[k]][j + y[k]] = 1
                    dfs(i + x[k], j + y[k], count + 1, p)
                    visit[i + x[k]][j + y[k]] = 0
            elif p > 0:
                if not visit[i + x[k]][j + y[k]]:
                    visit[i + x[k]][j + y[k]] = 1
                    dfs(i + x[k], j + y[k], count + 1, p - 1)
                    visit[i + x[k]][j + y[k]] = 0

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
answer = 0
n, m = map(int, input().split())
visit = [[0]*m for _ in range(n)]
miro = [[int(number) for number in input()] for _ in range(n)]
dfs(0, 0, 0, 1)
print(answer)