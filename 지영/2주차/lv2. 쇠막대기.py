def solution(tc):
    count = []
    result = 0
    for i in range(len(tc) - 1):
        # 레이저가 있으면 레이저로 만들어지는 막대의 수를 더함
        if tc[i] == '(' and tc[i + 1] ==')':
            result += len(count)
        # '('가 나오면 막대를 추가
        elif tc[i] == '(' :
            count.append(1)
        # ')'가 나오면 레이저로 자르고 난 후 남은 막대 추가
        elif tc[i] == ')' and tc[i + 1] == ')':
            result += count.pop()
    return result