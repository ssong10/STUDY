def solution(s):
    answer = True
    p = 0
    y = 0
    for char in s.lower():
        if char == 'p':
            p += 1
        elif char == 'y':
            y += 1
    if p != y:
        answer = False

    return answer
