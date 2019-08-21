def solution(n, lost, reserve):
    no = []
    for i in lost:
        if i not in reserve:
            no.append(i)
        else:
            reserve.remove(i)
    for j in no:
        if j-1 in reserve:
            n+=1
            reserve.remove(j-1)
        elif j+1 in reserve:
            n+=1
            reserve.remove(j+1)
    return n-len(no)