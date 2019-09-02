def solution(heights):
    n = len(heights)
    answer = [0] * n
    for i in range(n - 1, -1, -1):
        # 가장 뒤에 탑부터 pop을 해주며
        h = heights.pop()
        for j in range(len(heights)):
            # 탑의 높이 보다 큰 탑이 있을 경우
            if heights[len(heights) - j - 1] > h:
                # 수신한 탑의 인덱스를 추가해준다.
                answer[i] = len(heights) - j
                break
    return answer