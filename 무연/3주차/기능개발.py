def solution(progresses, speeds):
    answer = []
    result = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i]:
            result.append((100 - progresses[i]) // speeds[i] + 1)
        else:
            result.append((100 - progresses[i]) // speeds[i])
    days = result[0]
    count = 0
    for num in result:
        if num <= days:
            count += 1
        else:
            days = num
            answer.append(count)
            count = 1
    answer.append(count)
    return answer