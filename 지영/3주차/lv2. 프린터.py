from collections import deque

def solution(priorities, location):
    # 인덱스 list 생성
    idx = deque(list(range(len(priorities))))
    cnt = 0
    while True:
        # 처음 인덱스를 pop
        q = idx.popleft()
        # 처음 문서를 tmp에 저장
        tmp = priorities[q]
        for i in idx:
            # tmp보다 중요도가 큰 게 있으면
            if tmp < priorities[i]:
                # 다시 인덱스 list에 추가
                idx.append(q)
                break
        # 중요도가 큰 게 없다면
        else:
            # 출력한 문서의 개수를 더하고
            cnt += 1
            # 출력한 문서가 location의 인덱스와 같다면 break
            if q == location:
                break
    return cnt