def solution(arr):
    answer = 0
    s = 0
    for i in arr:
        s += i
    answer = s / len(arr)
    return answer