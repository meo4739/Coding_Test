n = int(input())
dp = []
for i in range(n):
    dp.append(list( map( int, input().split() ) ))

    
# dp[1] = [ dp[1][0] + dp[0][0]
#           dp[1][1] + dp[0][0],

# dp[2] = [ dp[2][0] + dp[1][0],

#           dp[2][1] + max( dp[1][0], dp[1][1] ),

#           dp[2][2] + dp[1][1] ]

# dp[3] = [dp[3][0] + dp[2][0],

#          dp[3][1] + max(dp[2][0], dp[2][1]),
#          dp[3][2] + max(dp[2][1], dp[2][2]),

#          dp[3][3] + dp[2][2]]


# dp[4] = [dp[4][0] + dp[3][0],

#          dp[4][1] + max(dp[3][0], dp[3][1]),
#          dp[4][2] + max(dp[3][1], dp[2][2]),
#          dp[4][3] + max(dp[3][2], dp[3][3]),

#          dp[4][4] + dp[3][3]
#          ]

# print(dp)

cnt = 2

print(dp)

for i in range(1,n):
    
    print(f"cnt : {cnt}")
    
    for j in range(cnt):
        
        # print(f"i, j {i},{j}")
        # print(f"dp[i][j] : {dp[i][j]}")
        
        if j==0:
            dp[i][j] = dp[i][j] + dp[i-1][j]
        
        elif j==i:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
            
        else:
            dp[i][j] = dp[i][j] + max( dp[i-1][j-1], dp[i-1][j]  )
            # print(dp[j])
    
    cnt+= 1
    
print(dp)   
print(max(dp[-1]))
    
    
    

