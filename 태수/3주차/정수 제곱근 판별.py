def solution(n):
    answer = 0
    x = n ** 0.5
    if not n % x :
        answer = (x+1)**2
    else:
        answer = -1
    return answer

print(solution(144))
