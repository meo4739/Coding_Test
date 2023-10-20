def solution(array, commands):

    
    answer = []
    
    for element in commands:

        # 슬라이싱 시작, 끝 범위 설정 => 정렬 => 숫자 선택
        # 인덱스는 0부터 시작
        # ex) 2번째 고르려면 2-1이 되어야 하므로 element[0]-1로 시작 설정

        answer.append(sorted(array[element[0]-1:element[1]])[element[2]-1])
    
    return answer


solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]] )