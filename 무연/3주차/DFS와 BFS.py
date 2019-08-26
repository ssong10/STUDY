import sys
from collection import deque
sys.setrecursionlimit(10000)




answer_dfs = []
answer_bfs = []
n, m, v = map(int, sys.stdin.readline().split())
u = [[] for _ in range(n)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    u[i].append(j)

for i in range(n):
    dfs(n)