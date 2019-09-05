from copy import deepcopy


def wall(dus, count):
    copy = deepcopy(dus)
    global answer
    if count == 3:
        c = cnt(vi(copy))
        if c > answer:
            answer = c
        return
    for i in range(n):
        for j in range(m):
            if not copy[i][j]:
                copy[i][j] = 1
                wall(copy, count + 1)
                copy[i][j] = 0


def cnt(dus):
    count = 0
    for i in range(n):
        for j in range(m):
            if not dus[i][j]:
                count += 1
    return count


def vi(dus):
    global visit
    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if dus[i][j] == 2 and not visit[i][j]:
                dus = dfs(i, j, dus)
    return dus


def dfs(i, j, dus):
    for k in range(4):
        if 0 <= i+x[k] < n and 0 <= j+y[k] < m:
            if not dus[i+x[k]][j+y[k]] and not visit[i+x[k]][j+y[k]]:
                visit[i + x[k]][j + y[k]] = 1
                dus[i + x[k]][j + y[k]] = 2
                dus = dfs(i + x[k], j + y[k], dus)
    else:
        return dus


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
answer = 0
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
wall(lab, 0)
print(answer)