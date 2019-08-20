def numbase(num_rule,call):
    result = [0,0]
    for i in range(3):
        if str(num_rule[0])[i] == call[i]:
            result[0] += 1
        elif call[i] in list(str(num_rule[0])):
            result[1] += 1
    if result == num_rule[1:3]:
        return True
    else:
        return False

def solution(baseball):
    result =0
    for x in range(1,10):
        for y in range(1,10):
            for z in range(1,10):
                if x!= y != z != x:
                    tmp = 0
                    for num_rule in baseball:
                        if numbase(num_rule,str(x)+str(y)+str(z)) == True :
                            tmp += 1
                    if tmp == len(baseball):
                        result += 1
    return result