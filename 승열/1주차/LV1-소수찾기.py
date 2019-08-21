def solution(n):
    sosu = [2]
    for i in range(3, n + 1):
        chk = True
        for j in sosu:
            if j > i ** (0.5):
                break
            if not i % j:
                chk = False
                break
        if chk == True:
            sosu.append(i)
    return len(sosu)

# def solution(n):
#     a = [False,False] + [True]*(n-1)
#     primes=[]

#     for i in range(2,n+1):
#         if a[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False
#     return len(primes)