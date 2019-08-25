def solution(s):
    answer = ''
    for i in range(len(s),0,-1):
        for j in range(1,i):
            if s[j-1] < s[j]:
                s[j-1], s[j] = s[j], s[j-1]
    answer = s
    return answer