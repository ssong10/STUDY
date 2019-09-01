from copy import deepcopy

def back(i, j, count, p_map):
    global answer
    copy_map = deepcopy(p_map)
    if count == n:
        answer += 1
        return
    else:
        for k in range(n):
            copy_map[i][k] = 1
            copy_map[k][j] = 1
            if i+k < n:
                if j+k < n:
                    copy_map[i + k][j + k] = 1
                if j-k >= 0:
                    copy_map[i + k][j - k] = 1
        for x in range(i + 1, n):
            for y in range(n):
                if copy_map[x][y] == 0:
                    back(x, y, count + 1, copy_map)
            else:
                return


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    answer = 0
    n_map = [[0]*n for _ in range(n)]
    for i in range(n):
        back(0, i, 1, n_map)
    print('#{} {}'.format(tc, answer))