def solution(prices):
    answer = []
    for i in range(len(prices)):
        if prices[i] == 1:
            answer.append(len(prices) - 1 - i)
        else:
            # i의 price가 j의 price보다 크면
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]:
                    # answer에 추가
                    answer.append(j - i)
                    break
            # 가격이 떨어지지 않는 경우에 길이만큼 추가
            else:
                answer.append(j - i)
    return answer