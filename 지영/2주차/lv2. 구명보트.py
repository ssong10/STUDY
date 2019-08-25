from collections import deque
# deque를 사용

def solution(people, limit):
    # 무게 순으로 사람을 정렬
    max_ = deque(sorted(people))
    count = 0
    # 가장 무거운 사람
    w = max_.pop()
    while max_:
        # 무게 제한을 넘지 않을 때 까지 무게가 작은 사람들을 추가
        if max_[0] + w <= limit:
            w += max_.popleft()
        # 무게 제한을 넘으면 보트 수 추가
        else:
            count += 1
            w = 0 if not max_ else max_.pop()
    return count + 1