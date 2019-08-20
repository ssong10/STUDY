def solution(participant, completion):
    answer = ''
    com = {}
    par = {}
    for name in completion:
        if name not in com:
            com[name] = 1
        else:
            com[name] += 1
    for name in participant:
        if name not in par:
            par[name] = 1
        else:
            par[name] += 1
    for name in par:
        if name not in com:
            answer = name
        elif par[name] != com[name]:
            answer = name
    return answer