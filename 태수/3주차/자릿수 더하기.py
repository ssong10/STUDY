def solution(n):
    answer = 0
    N = str(n)

    for i in N:
        answer += int(i)

    return answer

print(solution(123))