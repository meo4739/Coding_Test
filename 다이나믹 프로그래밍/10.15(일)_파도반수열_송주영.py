for i in range(int(input())):
    dp = [0, 1, 1, 1, 2, 2]
    
    n = int(input())

    if n <= 5:
        print(dp[n])
    
    else:          
        for j in range(6, n+1):
            
            dp.append(  dp[ - 1]  +  dp[-5]    )
            # print(dp)    
            
        
        print(dp[-1])
        
        


