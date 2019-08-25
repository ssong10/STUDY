def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        tmp = []
        for j in commands[i]:
            for k in range(array[j[0] - 1], array[j[1] - 1]):
                tmp.append(array[k])
            answer.append(sorted(tmp[j[2] - 1]))

    return answer