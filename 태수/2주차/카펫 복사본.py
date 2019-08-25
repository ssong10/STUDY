def solution(brown, red):
    answer = []
    num = brown + red
    arr = []
    for i in range(1, brown//2):
        if not num % i:
            arr.append(i)
    answer = [arr[-1], num // arr[-1]]
    return answer