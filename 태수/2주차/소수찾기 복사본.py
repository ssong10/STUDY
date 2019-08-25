# def solution(n): # n = 10
#     answer = 0
#     for d in range(n+1):
#         decimal = True
#         if d < 2:
#             decimal = False
#         elif d in (2, 3):
#             decimal = True
#         elif not d % 2 or not d % 3:
#             decimal = False
#         elif d < 9:
#             decimal = True
#         print(d, decimal)
#         if decimal:
#             answer += 1
#         else:
#             k, l = 5, n ** 0.5
#             while k <= l:
#                 if not d % k or not d % (k + 2):
#                     decimal = False
#                 k += 6
#             print(d, decimal)
#             if decimal:
#                 answer += 1
#
#     return answer
# print(solution(1000))
def solution(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 is 0 or n % 3 is 0:
        return False
    if n < 9:
        return True
    k, l = 5, n ** 0.5
    while k <= 1:
        if n % k is 0 or n % (k+2) is 0:
            return False
        k += 6
    return True

solution(10)

# 에라토스테네스의 체 해보기