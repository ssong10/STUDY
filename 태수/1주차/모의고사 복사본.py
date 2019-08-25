def solution(answers):
    answer = []
    a = []
    b = []
    c = []
    ac = 0
    bc = 0
    cc = 0
    d = [1, 3, 4, 5]  # d-0123, i-1357 9111315
    e = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answer)):
        a.append(1 + i % 5)
        if i & 1:
            b.append(d[(i // 2) % 4])
        else:
            b.append(2)
        c.append(e[i % 10])
    for j in range(len(answer)):
        if a[j] == answer[j]:
            ac += 1
        if b[j] == answer[j]:
            bc += 1
        if c[j] == answer[j]:
            cc += 1
    arr = [ac, bc, cc]
    tmp = ''
    for k in arr:
        tmp = arr[0]
        if arr[k] >= tmp:
            tmp = arr[k]

    return answer