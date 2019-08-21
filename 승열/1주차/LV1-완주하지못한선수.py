def solution(participant, completion):
    result = {}
    for i in participant:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1
    for j in completion:
        result[j] -= 1
    for idx, k in result.items():
        if k == 1:
            return idx