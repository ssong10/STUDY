def solution(baseball):
    answer = 0
    # 모든 조합의 리스트를 저장해주기 위한 리스트
    bb = []
    # 만들 수 있는 길이가 3인 모든 리스트를 만들어줌
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i != j and i != k and j != k:
                    bb.append(str(100*i+10*j+k))
    # bb리스트의 인덱스로 접근하여 비교해주기위한 리스트
    idx_list = [1] * len(bb)
    for case in range(len(bb)):
        for game in baseball:
            # 각각의 자리수에서 인덱스로 접근하기위해 string으로 바꿔줌
            game[0] = str(game[0])
            strike = 0
            ball = 0
            # 각각의 게임에서 스트라이크와 볼 갯수를 비교하며
            # 다른 경우엔 인덱스 리스트에서 0으로 바꿔줌
            for num in range(3):
                if game[0][num] == bb[case][num]:
                    strike += 1
                elif game[0][num] in bb[case]:
                    ball += 1
            if strike != game[1] or ball != game[2]:
                idx_list[case] = 0
    # 인덱스 리스트에서 1인 값의 갯수를 answer에 저장
    for num in idx_list:
        if num:
            answer += 1
    return answer