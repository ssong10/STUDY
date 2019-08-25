def solution(s):
    answer = ''
    tmp = ''
    for char in s:
        if char.isalpha():
            tmp += char
        else:
            tmp += ' '
            for idx,i in enumerate(tmp):
                if not idx & 1:
                    answer += i.upper()
                else:
                    answer += i.lower()

                tmp = ''

    for idx, j in enumerate(tmp):
        if not idx & 1:
            answer += j.upper()
        else:
            answer += j.lower()
        tmp = ''
    return answer
print(solution('aAaA   bBBBbaaa'))
