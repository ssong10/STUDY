seoul = ["jane", "Kim"]

def solution(seoul):
    answer = ''

    for idx in range(len(seoul)):
        if seoul[idx] == 'Kim':
            answer = idx
    return '김서방은 {}에 있다'.format(answer)

print(solution(seoul))