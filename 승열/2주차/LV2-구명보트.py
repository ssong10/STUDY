def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    fat =0
    while len(people) > fat:
        if people[fat] + people[-1] <= limit:
            people.pop()
        fat +=1
        answer += 1
    return answer