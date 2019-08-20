def solution(people, limit):
    answer = 0
    # 정렬
    people.sort()
    # 좌우 인덱스로 접근하여 값을 불러오기 위해 추가
    i, j = 0, len(people) - 1
    # 가장 작은 값부터 작은 값을 기준으로
    # 큰 값을 점점 줄여나가며(-1) limit이하의 값을 찾음
    # limit 이하의 값이 나올경우 i에 1을 더해줌
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            answer += 1
        else:
            j -= 1
            answer += 1
    return answer