from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    end = [] # 도착한 트럭
    answer = 0 # 초 단위
    i = 0 # 출발트럭갯수
    while end != truck_weights: # 트럭 도착 다 안했으면

        if bridge[0] != 0: # 다리 끝이 트럭이면 end에 추가, 다리끝이 없으면 빼준다.
            end.append(bridge.popleft())
        else:
            bridge.popleft()
            
        if i != len(truck_weights) and sum(bridge) + truck_weights[i] <= weight: 
            bridge.append(truck_weights[i])
            i +=1
        else:
            bridge.append(0)

        answer += 1
    return answer