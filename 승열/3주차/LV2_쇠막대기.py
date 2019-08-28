def solution(arrangement):
    stack = []
    result = 0
    tmp = 0
    for i in arrangement:
        if i == '(':
            stack.append('(')
            tmp = 1 
        else:
            if stack[-1] =='(' and tmp ==1:
                result += len(stack)-1
            else:
                result += 1
            stack.pop()
            tmp = 0
    return result