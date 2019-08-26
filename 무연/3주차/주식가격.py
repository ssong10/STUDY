def solution(prices):
    answer = [0]
    numbers = []
    numbers.append(prices.pop())
    for _ in range(len(prices)):
        count = 0
        for i in range(len(numbers) - 1, -1, -1):
            count += 1
            if prices[-1] > numbers[i]:
                break
        numbers.append(prices.pop())
        answer.append(count)
    answer.reverse()
    return answer