# def solution(n, m):
#     answer = []
#     Max = []
#     MMax = []
#     for i in range(1, n+1):
#         if not n % i:
#             Max.append(i)
#     for j in range(1, m+1):
#         if not m % j:
#             MMax.append(j)
#     a = max(set(Max) & set(MMax))
#     print(Max, MMax)
#     answer.append(a)
#     Min = []
#     MMin = []
#     z = 1
#     while not bool(set(Min) & set(MMin)):
#         Min.append(n*z)
#         MMin.append(m*z)
#         print(Min, MMin)
#         if bool(set(Min) & set(MMin)):
#             answer.append(min(set(Min) & set(MMin)))
#             break
#         z+=1
#
#     return answer
#
# print(solution(2, 5))
# 유클리드 호제법
# answer = []
# def solution(n, m):
#     while m:
#         n, m = m, n % m
#     return answer.append(n)
# print(solution(10,12))
# print(answer)
# def solution2(n, m):
#     lcm = (n*m) // solution(n, m)
#     return lcm
#
# print(solution(10,12), solution2(10, 12))
