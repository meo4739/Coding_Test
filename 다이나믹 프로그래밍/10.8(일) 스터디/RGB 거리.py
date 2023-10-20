# 반복 횟수 repetition
repetition = int(input()) 

# 색을 담을 공간 color
color = []

# 정수형의 리스트로 color 공간 채우기
for col in range(repetition):
    color.append( list( map( int, input().split() ) ) ) 

# 계산 공간 calculation
calculation = [[0]*3 for _ in range(repetition)]

# 처음 공간은 제일 처음에 받은 값으로 채우기
calculation[0][0] = color[0][0]
calculation[0][1] = color[0][1]
calculation[0][2] = color[0][2]


# 계산
for i in range(1, repetition):
    
    
    # ( 현재 색칠 비용 ) + ( 위의 계산값이 들어 있는 칸에서 현재 칸과 다른 위치의 칸의 값 중 min 값 )
    calculation[i][0] = color[i][0] + min( calculation[i-1][1], calculation[i-1][2] )
    calculation[i][1] = color[i][1] + min( calculation[i-1][0], calculation[i-1][2] )
    calculation[i][2] = color[i][2] + min( calculation[i-1][0], calculation[i-1][1] )
    

print("calculation:\n",calculation)
print( min(calculation[-1]) )