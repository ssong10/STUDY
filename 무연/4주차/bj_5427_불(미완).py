import sys
from collections import deque
I = sys.stdin.readline


def bfs(i, j):
    count = 0
    cbd[i][j] = '*'
    esc = deque()
    esc.append((i, j))
    while esc:
        count += 1
        for _ in range(len(esc)):
            u, v = esc.popleft()
            if u == 0 or v == 0 or u == h-1 or v == w-1:
                return count
            for n in range(4):
                if 0 <= u+x[n] < h and 0 <= v+y[n] < w:
                    if cbd[u+x[n]][v+y[n]] in '.@':
                        esc.append((u+x[n], v+y[n]))
                        cbd[u + x[n]][v + y[n]] = '*'
    return 0xffff


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
t = int(input())
for tc in range(t):
    w, h = map(int, input().split())
    bd = [list(I()) for _ in range(h)]
    fire_count = 0
    human_count = 0
    for i in range(h):
        for j in range(w):
            if bd[i][j] == '*':
                cbd = [list(line) for line in bd]
                fire_count = bfs(i, j)
            if bd[i][j] == '@':
                cbd = [list(line) for line in bd]
                human_count = bfs(i, j)
    if human_count < fire_count:
        print(human_count)
    else:
        print('IMPOSSIBLE')