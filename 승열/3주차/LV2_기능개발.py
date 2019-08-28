def solution(progresses, speeds):
    result = []
    N = len(progresses)
    n = 0
    while sum(result) != N:
        tmp = 0
        for i in range(N):
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                speeds[i] = 0
        for cmd in progresses[n:]:
            if cmd >= 100:
                tmp += 1
            else:
                break
        if tmp >0:
            result.append(tmp)
            n += tmp
    return result