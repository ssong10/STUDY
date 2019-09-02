def solution(tc):
    count = []
    result = 0
    for i in range(len(tc) - 1):
        # 레이저가 나오면 길이를 더해주고
        if tc[i] == '(' and tc[i + 1] ==')':
            result += len(count)
        # '('가 나오면 막대를 추가
        elif tc[i] == '(' :
            count.append(1)
        # ')'가 나오면 막대를 빼줌
        elif tc[i] == ')' and tc[i + 1] == ')':
            result += count.pop()
    return result