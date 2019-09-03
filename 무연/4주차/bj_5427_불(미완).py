import sys
from copy import deepcopy
I = sys.stdin.readline

def simulation():
    count = 1
    answer = 1
    while count:
        count = 0
        past = deepcopy(room)
        for i in range(h):
            for j in range(w):
                if past[i][j] == '@':
                    if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                        return answer
                    count += human(i, j, past)
        for i in range(h):
            for j in range(w):
                if past[i][j] == '*':
                    fire(i, j, past)
        answer += 1
    return 'IMPOSSIBLE'


def human(i, j, past):
    count = 0
    for k in range(4):
        if 0 <= i + x[k] < h and 0 <= j + y[k] < w:
            if past[i + x[k]][j + y[k]] == '.':
                room[i + x[k]][j + y[k]] = '@'
                count += 1
    return count


def fire(i, j, past):
    for k in range(4):
        if 0 <= i + x[k] < h and 0 <= j + y[k] < w:
            if past[i + x[k]][j + y[k]] != '#':
                room[i + x[k]][j + y[k]] = '*'


x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    w, h = map(int, I().split())
    room = [list(I()) for _ in range(h)]
    print(simulation())