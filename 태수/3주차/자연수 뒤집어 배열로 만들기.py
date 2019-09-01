def solution(n):
    answer = []
    ls = []
    for i in str(n):
        ls.append(i)
    while ls:
        answer.append(int(ls.pop()))

    return answer

print(solution(12345))