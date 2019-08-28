def solution(prices):
    N = len(prices)
    stack = []
    for i in range(N):
        tmp = 0
        for j in range(1,N-i):
            tmp +=1
            if prices[i] <= prices[i+j]:
                pass
            elif prices[i] > prices[i+j]:
                break
        stack.append(tmp)
    return stack