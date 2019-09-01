def solution(d, budget):
    answer = 0
    d.sort()
    count = 0
    s = []
    S = []
    tmp = []
    for x in range(1 << len(d)):
        for y in range(len(d)+1):
            if x & (1<<y):
                tmp.append(d[y])
        # if sum(tmp) == budget:
        #     s.append(tmp)
        #     print(tmp)
        # for k in tmp:
        #     S = len(k)
        #
        # for j in s:
        #     if len(j) == max(S):
        #         count += 1
        # print(count)
        # return answer

solution(([1,2,3,4,5]),9)