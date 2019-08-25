def solution(s):
    answer = True

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isdecimal():
                answer = True
            else:
                answer = False
                break
    else:
        answer = False

    return answer