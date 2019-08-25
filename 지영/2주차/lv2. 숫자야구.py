def solution(baseball):
    answer = 0
    # 1 부터 9까지 각기 다른 수를 가진 세자리 자연수 만들기
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and j != k and k != i:
                    num = [i, j, k]
                    result = True
                    for case in baseball:
                        strike = ball = 0
                        ques = [int(i) for i in str(case[0])]
                        # 질문에 있는 수를 하나씩 불러옴
                        for l in range(3):
                            # 위치와 수가 같으면 strick
                            if num[l] == ques[l]:
                                strike += 1
                            # 해당하는 수가 만든 자연수에 포함되어 있으면 ball
                            elif ques[l] in num:
                                ball += 1
                        # 하나라도 일치하지 않으면 False
                        if strike != case[1] or ball != case[2]:
                            result = False
                    # 모두 일치하는 경우 answer에 추가
                    if result:
                        answer += 1
    return answer