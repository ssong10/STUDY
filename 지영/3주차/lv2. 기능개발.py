from collections import deque
def solution(progresses, speeds):
    answer = deque([])
    progresses, speeds = deque(progresses), deque(speeds)
    # progresses의 가장 앞에 있는 기능이 100을 넘을 때 까지 speeds를 더해준다
    while progresses:
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        count = 0
        # 가장 앞에 있는 기능이 100을 넘으면 100을 넘은 기능들을 차례로 빼준다.
        while progresses[0] > 99:
            speeds.popleft()
            progresses.popleft()
            count += 1
            # 기능이 모두 빠져나가면 멈추고
            if not progresses:
                break
        # 빼준 기능의 개수를 result에 더해준다.
        if count:
            answer.append(count)
    return list(answer)