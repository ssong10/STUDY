def solution(participant, completion):
    participant.sort()
    completion.sort()
    # 두 list를 정렬하여 하니씩 비교하면서 서로 같지 않은 이름이 나왔을 때 반환
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]