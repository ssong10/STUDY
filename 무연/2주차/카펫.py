def solution(brown, red):
    # 사각형이 될 수 있는 모든 경우의 수를 저장하기위한 리스트
    sqr_list = []
    # 가로 == 세로가 되는 지점, 정사각형이 되는 경우
    # 너비의 제곱근이 되므로 제곱근 이하의 값까지만 반복
    for number in range(1, int((brown + red)**(1/2))+1):
        if not (brown+red) % number:
            sqr_list.append([(brown+red) // number, number])
    # 갈색 영역의 경우 가로x2 + 세로x2 - 4 이므로
    # 이값을 이용해 정답 리스트를 찾아줌
    for num_list in sqr_list:
        if num_list[0] * 2 + num_list[1] * 2 - 4 == brown:
            answer = num_list
    return answer