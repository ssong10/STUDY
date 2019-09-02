from collections import deque 
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    # 빈 덱을 만들어 다리를 만든다
    bridge = deque([])
    sec = w = 0
    while truck_weights:
        sec += 1
        # 다리 길이와 다리가 같아 졌을 때 다리에서 트럭을 빼준다
        if len(bridge) == bridge_length:
            w -= bridge.popleft()
        # 다리가 다리 길이보다 작을 때
        if truck_weights[0] + w <= weight:
            # 트럭의 무게가 제한 무게를 넘지 않으면 트럭을 추가하고
            tmp = truck_weights.popleft()
            bridge.append(tmp)
            w += tmp
        # 제한 무게를 넘으면 0을 추가 
        else:
            bridge.append(0)

    return sec + bridge_length