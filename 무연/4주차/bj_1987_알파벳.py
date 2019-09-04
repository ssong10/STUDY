def dfs(i, j, count, word):
    global answer
    if answer < count:
        answer = count
    word += alph[i][j]
    for k in range(4):
        if 0 <= i+x[k] < r and 0 <= j+y[k] < c:
            if alph[i+x[k]][j+y[k]] not in word:
                dfs(i+x[k], j+y[k], count + 1, word)


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
r, c = map(int, input().split())
alph = [list(input()) for _ in range(r)]
answer = 0
dfs(0, 0, 1, '')
print(answer)