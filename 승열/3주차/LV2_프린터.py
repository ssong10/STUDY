from collections import deque
def solution(priorities, location):
    Q = deque(priorities)
    idx = deque(range(len(priorities)))
    find = idx 
    result = [] #인덱스를 저장
    while not location in result:
        mx = max(Q)
        Qout = Q.popleft()
        idxout = idx.popleft()
        if Qout == mx:
            result.append(idxout)
        else:
            Q.append(Qout)
            idx.append(idxout)
    return len(result)