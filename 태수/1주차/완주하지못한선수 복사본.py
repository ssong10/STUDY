def solution(participant, completion):
    answer = ''
    a = set(participant)
    b = set(completion)
    if len(a) > len(b):
        answer = ''.join(a - b)
    else:
        for c in completion:
            if c in participant:
                participant.remove(c)
        answer = ''.join(participant)

    return answer