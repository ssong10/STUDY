def solution(n):
    answer = 0
    # 2~n까지의 모든 숫자 set
    num_set = set([number for number in range(2, n + 1)])
    # 소수가 아닌수를 저장해주기위한 set
    n_set = set([0])
    for number in range(2, n + 1):
        for mul in range(2, n):
            # n_set에 없는 값의 배수들을 저장
            if number * mul > n and number * mul not in n_set:
                break
            else:
                n_set.add(number * mul)
    # 차집합의 길이 리턴
    answer = len(num_set - n_set)
    return answer