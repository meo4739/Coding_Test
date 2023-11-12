import sys
sys.stdin = open('./그리디/백준/블로그2.txt')

n = int(input())
color = input()


# B를 메인 색깔로 한다.
# 색깔의 변화가 있는데 바뀐 색상이 B가 아니면 횟수를 1회 추가한다.
# 시작점이 B가 아니었다면, R -> B로 갈 때 count가 되지 않으므로 별도의 if문인 if color[0] !=  'B'를 추가해준다.
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