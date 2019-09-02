from collections import deque

def BFS():
    result = 0
    while tmp:
        print(tmp)
        result += 1
        for _ in range(len(tmp)):
            A = tmp.popleft()
            if A[:2] ==[N-1,M-1]:
                return result
            y,x = A[0],A[1]
            for d in range(4):
                # 벽부 가능, 안부실때
                if -1 < y + dy[d] < N and -1 < x + dx[d] < M and visit[y + dy[d]][x + dx[d]][1] == 0 and maze[y + dy[d]][x + dx[d]] == 0 and A[2]:
                    tmp.append([y+dy[d],x+dx[d],A[2]])
                    visit[y+dy[d]][x+dx[d]] = [1,1]

                # 벽부가능, 부셔야할때
                if -1 < y + dy[d] < N and -1 < x + dx[d] < M and visit[y + dy[d]][x + dx[d]][1] == 0 and maze[y + dy[d]][x + dx[d]] == 1 and A[2]:
                    if [y+dy[d],x+dx[d],0] in tmp:

                        tmp.append([y+dy[d],x+dx[d],A[2]-1])
                    visit[y+dy[d]][x+dx[d]] = [1,1]

                # 벽부 못할때
                if -1< y + dy[d] < N and -1 < x+dx[d] < M and visit[y+dy[d]][x+dx[d]][0] == 0 and maze[y+dy[d]][x+dx[d]] == 0:
                    tmp.append([y+dy[d],x+dx[d],0])
                    visit[y+dy[d]][x+dx[d]][0] = 1
    return -1

N, M = map(int,input().split())
maze = []
visit = [[[0,0] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    maze.append(list(map(int,input())))
tmp = deque([[0,0,1]])
visit[0][0] = [1,1]
dy = [1,-1,0,0]
dx = [0,0,1,-1]
print(BFS())