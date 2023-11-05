import sys
sys.stdin = open('./그리디/강의/섹션 4/7. 창고 정리/창고정리.txt','r')

length = int(input()) # 가로 길이

space = list(map(int, input().split() )) # 상자 입력
print(space)
space.sort() # 그리디 문제이니까 정렬한다.
print(space)

for i in range(int(input())): # 상자 조정 횟수 만큼 반복문 실행한다.
    space[0]+=1  # 가장 작은 거는 1을 더한다.
    space[-1]-=1 # 가장 큰 거는 1을 뺀다.
    space.sort()

# print(space)
print(space[-1]-space[0])

