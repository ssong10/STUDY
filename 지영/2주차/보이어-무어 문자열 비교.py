T = int(input())
for tc in range(T):
    print('#{}'.format(tc + 1), end = ' ')
    N = input()
    M = input()
    i = 0
    idx = len(N) - 1
    result = 0
    while i < len(M) - len(N) + 1:
        if M[i + idx] != N[idx]:
            for j in range(idx, -1, -1):
                if N[j] == M[i + idx]:
                    i += idx - j
                    break
            else:
                i += len(N)
        else:
            for k in range(idx - 1, -1, -1):
                if M[i + idx - k] != N[idx - k]:
                    i += 1
                    break
            else:
                result = 1
                break
    print(result)