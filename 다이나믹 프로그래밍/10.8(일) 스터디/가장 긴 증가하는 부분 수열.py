# 수열 길이 length
length = int(input())

# 계산할 수열을 number에 넣기
# 뒤에서 선택 숫자와 앞의 숫자를 비교하는 for문을 위해 앞에 [0]을 앞에 추가
numbers = [0] + list( map ( int, input().split() ))
    
print(numbers) # 확인

# 수열 길이 계산용 count 생성
count = [0] * (length+1)


# 전체 진행
# 앞의 숫자와 비교하는 과정이 계속 진행해야 하므로 1부터 시작
# 1 ~ length까지 진행되어야 하므로 "length + 1"
for num1 in range(1,length+1):
    
    # 길이 계산용 초기값
    cnt = 0
    
    # 선택 숫자의 앞의 숫자들과 비교
    for num2 in range(0, num1):
        
        # 앞에 숫자들 중에서 선택 숫자보다 더 작은 값이 있는지 확인
        if numbers[num1] > numbers[num2]:
        # 더 작은 값이 있다면,
            cnt = max(cnt, count[num2])
                       
    # 가장 처음은 1이 될 것
    count[num1] = cnt+1

            # (ex)
            # numbers [0 10 20 30 20 ], count = [0 1 2 3 2]
            # 마지막 부분을 생각하면,
            # numbers[5](=20) 보다 작은 값은 numbers[1]만 존재
            # 따라서 count[1]에 저장된 값(1)에서만 +1 => 2가 "5" 공간에 채워진다.
            # 계산 공간인 count 계속 채우기
            

# 가장 큰 값이 가장 긴 수열의 길이
print(max(count))

