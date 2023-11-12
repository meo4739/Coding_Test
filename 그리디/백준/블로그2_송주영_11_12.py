import sys
sys.stdin = open('./그리디/백준/블로그2.txt')

# 갯수를 입력 받고, 색깔을 입력받자
n = int(input())
color = input()

# B를 메인 색깔로 작업할 때와 R을 메인 색깔로 작업할 때 중에서 최소인 것을 계산하자

# B를 메인 색깔로 한다.
# 색깔의 변화가 있는데 바뀐 색상이 B가 아니면 횟수를 1회 추가한다.
# 시작점이 B가 아닌 경우는 if color[0] !=  'B'를 통해 1회 추가한다.
# 예를 들어 RRRBBB인 경우를 생각해보자
# 시작 색깔을 따지지 않으면 R로 칠하는 경우의 수가 누락된다.
answer_B = 1
for i in range(1,n):
    if (color[i-1] != color[i]) & (color[i] != "B"):
        answer_B+=1
    if color[0] != "B":
        answer_B+=1

# R를 메인 색깔로 한다.
# 색깔의 변화가 있는데 바뀐 색상이 R가 아니면 횟수를 1회 추가한다.
# 시작점이 R가 아니었다면, B -> R로 갈 때 count가 되지 않으므로 별도의 if문인 if color[0] !=  'R'를 추가해준다.
answer_R = 1
for i in range(1,n):
    if (color[i-1] != color[i]) & (color[i] != "R"):
        answer_R+=1
    if color[0] != "R":
        answer_R+=1

print(min(answer_B, answer_R))