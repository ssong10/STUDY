from collections import deque


def solution(priorities, location):
    answer = 0
    pri = deque(priorities)
    idx = deque([0] * len(priorities))
    idx[location] = 1
    que_list = []
    while True:
        max_idx = 0
        max_value = pri[0]
        for i in range(len(pri)):
            if pri[i] > max_value:
                max_value = pri[i]
                max_idx = i
        for i in range(max_idx):
            pri.append(pri.popleft())
            idx.append(idx.popleft())
        pri.popleft()
        num = idx.popleft()
        if num == 1:
            answer += 1
            break
        else:
            answer += 1

    return answer