def solution(num):
    answer = 0
    i = 0
    while i < 500:
        if num == 1:
            return 0
        i += 1
        if num & 1:
            num = num * 3 + 1
        else:
            num = num // 2
        if num == 1:
            answer = i
            break
        elif i == 500:
            answer = -1
    return answer

solution(102)