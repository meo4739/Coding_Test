import sys
sys.stdin = open('./그리디/강의/섹션 4/5_회의실 배정/회의실.txt','r')
space = []

for i in range(int(input() )):
    space.append(list(map( int, input().split())))

print(space)
space.sort() # 첫 번째를 기준으로 정렬한다.
print(space)
space.sort(key = lambda x : (x[1], x[0])  ) # 두 번째를 기준으로 정렬한다.
print(space)

time = 0
cnt = 0
for s, e in space:
    if s >= time: # 시작 시간이 이전 시간의 마감 시간보다 크다면 마감 시간을 바꾸고 cnt를 늘린다.
        time = e
        cnt += 1

print(cnt)