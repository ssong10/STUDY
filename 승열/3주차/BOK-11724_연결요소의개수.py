def DFS(i):
    for j in V[i]:
        if visit[j] == False:
            visit[j] = True
            DFS(j)
            

N,M  = map(int,input().split())
visit = [False] * (N+1)
V = [[] for _ in range(N+1)]
for _ in range(M):
    v,u = map(int,input().split())
    V[v] = u
    V[u] = v
result = 0
for i in range(1,len(visit)+1):
    if visit[i] == False:
        result+=1
        DFS(i)
print(result)