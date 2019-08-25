# 시간 초과 해결
def solution(n):
    # n까지의 수가 담겨 있는 집합 count 생성
    count = set(range(2, n+1))
    # 소수를 저장하는 list 생성
    nums = [2]
    for i in range(3, n + 1):
        if i in count:
            # i가 count에 있으면 i의 배수들을 count에서 빼고 소수통에 추가
            count -= set(range(nums[-1], n+1, nums[-1]))
            nums.append(i)
    return len(nums)