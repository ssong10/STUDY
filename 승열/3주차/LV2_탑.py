def solution(heights):
    N = len(heights)
    stack = []  
    result = []
    for i in range(len(heights)-1,-1,-1): # 4,3,2,1,0
        while stack and heights[i] > stack[-1]:
            result.append(i+1)
            stack.pop()
        stack.append(heights[i])
        if heights[i] == max(heights[:i+1]):
            result.append(0)
    return result[::-1]