def solution(x):
    answer = True
    a = list(str(x))
    s = 0

    for i in a:
        s += int(i)
    if not x % s:
        return True

    return False

print(solution(123))