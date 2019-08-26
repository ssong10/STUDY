def solution(arrangement):
    answer = 0
    r = 0
    arr = list(arrangement)
    p = []
    p.append(arr.pop())
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == '(' and r == 0:
            arr.pop()
            p.pop()
            answer += len(p)
            r = 1
        elif arr[i] == '(':
            arr.pop()
            p.pop()
            answer += 1
        else:
            p.append(arr.pop())
            r = 0
    return answer