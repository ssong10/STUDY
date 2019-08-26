import sys
sys.setrecursionlimit(10000)

def DFS(i, j):
    global c
    c += 1
    apart_list[i][j] = 0
    for num in range(4):
        if -1 < i+x[num] < n and -1 < j+y[num] < n:
            if apart_list[i+x[num]][j+y[num]]:
                DFS(i+x[num], j+y[num])

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
n = int(sys.stdin.readline())
apart = []
apart_list = []
for _ in range(n):
    apart += list(map(str, sys.stdin.readline().split()))
for num in apart:
    apart_list.append([int(number) for number in num])
count = 0
danji = []
for i in range(n):
    for j in range(n):
        c = 0
        if apart_list[i][j]:
            DFS(i, j)
            danji.append(c)
            count += 1
print(count)
danji.sort()
for num in danji:
    print(num)