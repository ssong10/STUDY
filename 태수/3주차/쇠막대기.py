def solution(arrangement):
    answer = 0
    S = []
    arrangement = arrangement.replace('()','a')
    for i in arrangement:
        if i == '(':
            S.append(i)
        elif i == ')':
            S.pop()
            answer += 1
        elif i =='a':
            answer += len(S)

    return answer

solution('()(((()())(())()))(())')