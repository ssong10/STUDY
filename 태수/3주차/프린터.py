def solution(priorities, location):
    answer = 0
    S = []
    A = []
    for i in range(len(priorities)):
        if max(priorities[i]) == i:
            S.append(priorities[i])
        else:
            A.append(i)


    return answer