def solution(arr, divisor):
    answer = []
    for i in arr:
        if not i % divisor:
            answer.append(i)
    if not len(answer) >= 1:
        answer.append(-1)

    for j in range(len(answer),0,-1):
        for k in range(1,j):
            if answer[k-1] > answer[k]:
                answer[k-1],answer[k] = answer[k],answer[k-1]
    return answer