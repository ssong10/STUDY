from collections import deque

def bfs(i, j, count):
    now = deque()
    now.append((i, j))
    miro[i][j] = 0
    while now:
        count += 1
        for _ in range(len(now)):
            u, v = now.popleft()
            if (u, v) == (n-1, m-1):
                return count
            for a in range(4):
                if 0 <= u + x[a] < n and 0 <= v + y[a] < m:
                    if miro[u + x[a]][v + y[a]]:
                        miro[u + x[a]][v + y[a]] = 0
                        now.append((u + x[a], v + y[a]))


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
n, m = map(int, input().split())
miro = [[int(number) for number in input()] for _ in range(n)]
print(bfs(0, 0, 0))