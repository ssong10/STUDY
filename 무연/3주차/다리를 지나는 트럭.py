from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    crossing = deque([])
    crossing.append(truck_weights.popleft())
    time = deque([1])
    while crossing or truck_weights:
        if time[0] == bridge_length:
            crossing.popleft()
            time.popleft()
        if truck_weights and sum(crossing) + truck_weights[0] <= weight:
            crossing.append(truck_weights.popleft())
            time.append(0)
        for i in range(len(time)):
            time[i] += 1
        answer += 1

    return answer