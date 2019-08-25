def solution(strings, n):
    answer = []
    tmp = strings[0]
    result = True
    for string in strings[1:]:
        # 문자열의 n번째 문자의 크기를 비교하여 answer 리스트에 추가
        if string[n] < tmp[n] or string[n] == tmp[n] and string < tmp:
            answer.append(string)
            # 문자열의 순서가 바뀌면 False를 result에 저장하여
            result = False
        else:
            answer.append(tmp)
            tmp = string
    answer.append(tmp)
    if result:
        return answer
    # 바뀌지 않을 때 까지(정렬 될 때 까지) 재귀
    return solution(answer, n)