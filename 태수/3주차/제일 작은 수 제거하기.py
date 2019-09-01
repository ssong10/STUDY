def solution(arr):
    answer = []
    x = min(arr)
    if len(arr) == 1:
        answer.append(-1)
    else:
        arr.remove(x)
        answer = arr
    return answer
