import sys
sys.stdin = open('./그리디/강의/섹션 4/6. 씨름선수/씨름선수.txt','r')
# sys.stdin = open('./그리디/강의/섹션 4/6. 씨름선수/in1.txt', 'r')

space = [] # 값들을 넣자.
for _ in range(int(input())):
    space.append(list(map(  int, input().split() )))

print(space) # 처음 상태를 확인하자
space.sort(reverse = True) # 키 순서로 내림차순 정렬한다.
print(space) # 정렬 상태를 확인하자

cnt = 0
heavy = 0 # 현재 선택된 선수의 몸무게와 이전 선수들의 몸무게를 비교하여 가장 큰 값 저장

for height, weight in space:
    if weight > heavy: # 현재 선택된 선수의 몸무게와 이전 선수들의 몸무게를 비교
        heavy = weight # 현재 값으로 heavy 값을 업데이트 한다.
        cnt +=1

print(cnt)


