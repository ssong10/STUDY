def solution(n):
    answer = 0
    a = []
    b = 0
    for i in str(n):
        a.append(i)
    for j in range(len(a)-1, 0, -1):
        for k in range(0, j):
            if a[k+1] >= a[k]:
                a[k], a[k+1] = a[k+1], a[k]
    b = ''.join(a)
    answer = int(b)
    return answer

print(solution(12345))