def solution(phone_number):
    answer = ''
    a = list(str(phone_number))
    answer += '*' * (len(a)-4)
    for i in range(len(a)-4, len(a)+1):
        answer += a[i]

    return answer

