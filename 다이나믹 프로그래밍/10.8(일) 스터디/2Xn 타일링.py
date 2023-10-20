
def fibo(num):

    # 0으로 계산 결과 담을 공간 채워두기
    dp = [0 for i in range(num+1)]

    # 계산을 위해 앞에 2개는 1로 채워두기
    dp[0], dp[1] = 1, 1

    # 2번째부터는 앞에 두 개를 더하는 계산 시작
    if num>=2:
        
        for cal in range(2,num+1):
            
            # 앞에 두 개를 더한 값으로 계산 결과 담는 공간을 채워나간다.
            dp[cal] = dp[cal-1] + dp[cal-2]
            
    
    # 확인용
    print("num:",num)        
    print("dp",dp)
    
    # 계산 결과 값을 10,007나눈 나머지 반환
    
    return dp[num]%10007
    
print(fibo(int(input())))


