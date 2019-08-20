def solution(brown, red):
    N = (brown + 4)//2
    for i in range(N):
        if i * (N-i) == brown+red:
            return [N-i,i]