import sys
sys.setrecursionlimit(10000)
def DFS(i):
    used[i] = 0
    for j in trees[i]:
        if used[j]:
            DFS(j)


answer = 0
n, m = map(int, sys.stdin.readline().split())
in_list = []
used = [0] + [1] * n
trees = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    trees[u].append(v)
    trees[v].append(u)
for i in range(n + 1):
    if used[i]:
        DFS(i)
        answer += 1

print(answer)