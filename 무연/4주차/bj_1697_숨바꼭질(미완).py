import sys
sys.setrecursionlimit(100000)
def back(r, count):
    global min_num
    if min_num < count:
        return
    elif count > abs(k - n):
        return
    elif r == k:
        if count < min_num:
            min_num = count
        return
    else:
        for i in range(3):
            if i == 0:
                back(r + 1, count + 1)
            elif i == 1:
                back(r - 1, count + 1)
            elif i == 2:
                back(r * 2, count + 1)


n, k = map(int, input().split())
min_num = 0xffffff
result = []
back(n, 0)
print(min_num)