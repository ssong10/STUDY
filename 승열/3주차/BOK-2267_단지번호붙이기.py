def DPS(x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    house[y][x] = '0'
    tmp.append(1)
    for i in range(4):
        if -1 < x + dx[i] < n and -1 < y + dy[i] < n and house[y+dy[i]][x+dx[i]] != '0':
            DPS(x+dx[i], y+dy[i])

n = int(input())
house = [list(input()) for _ in range(n)]
result = []
for y in range(n):
    for x in range(n):
        if house[y][x] != '0':
            tmp = []
            DPS(x,y)
            result.append(len(tmp))
print(len(result))
for i in sorted(result):
    print(i)