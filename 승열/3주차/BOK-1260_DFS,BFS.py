def DFS(V):
    visit[V] = True
    DFS_result.append(V)
    for i in web[V]:
        if visit[i] == False:
            DFS(i)
def BFS():
    while tmp:
        a = tmp.pop(0)
        BFS_result.append(a)
        for i in web[a]:
            if visit2[i] == False:
                visit2[i] = True
                tmp.append(i)


N, M ,V = map(int,input().split())
web = [[] for _ in range(N+1)]
visit = [False] * (N+1)
visit2 = [False] * (N+1)
visit2[V] = True

for _ in range(M):
    v,u = map(int,input().split())
    web[v].append(u)
    web[u].append(v)
for point in web:
    point.sort()

DFS_result=[]
DFS(V)
print(DFS_result)


BFS_result=[]
tmp = [V]
BFS()
print(BFS_result)