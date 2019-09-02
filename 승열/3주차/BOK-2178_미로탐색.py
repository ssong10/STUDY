from collections import deque
import sys
ip = sys.stdin.readline

def BFS():
    result = 1
    while tmp:
        result += 1
        for _ in range(len(tmp)):
            y,x = tmp.popleft()
            for d in range(4): 
                if -1< y+dy[d] < N and -1 < x+dx[d] < M and visit[y+dy[d]][x+dx[d]] == 0 and miro[y+dy[d]][x+dx[d]] == '1':  
                    visit[y+dy[d]][x+dx[d]] = result
                    tmp.append((y+dy[d],x+dx[d]))
    print(visit)
    print(visit[N-1][M-1])

N, M = map(int,ip().split())
miro = []
for _ in range(N):
    miro.append(list(ip()))
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1
tmp = deque([[0,0]])
dy = [-1, 1, 0, 0]
dx = [0,0,-1,1]
BFS()