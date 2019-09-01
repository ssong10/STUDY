def solution(arr1, arr2):
    answer = [[]*len(arr1)]

    for i in range(len(arr1)):

        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j]+arr2[i][j]

    return answer

# a = [[]]
# a = [[1,2],[3,4]] + [[1,3],[4,1]]
# print(a)