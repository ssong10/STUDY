# 처음 풀이(갈색 카펫이 한 줄이 아닐 경우)
def solution(brown, red):
    rw, rh = red, 1
    while rw >= rh:
        bw, bh = rw + 2, rh +2
        carpet = brown
        while carpet > 0:
            carpet -= (bw + bh) * 2 - 4
            if carpet == 0:
                return [bw, bh]
            bw += 2
            bh += 2
        for i in range(rh + 1, rw + 1):
            if not red % i:
                rh = i
                rw = red//i
                break



# 갈색 카펫이 한 줄일 경우
def solution(brown, red):
    for i in range(1, red + 1):
        if not red % i and (i + red//i)*2 + 4 == brown:
            return [red//i + 2, i + 2]