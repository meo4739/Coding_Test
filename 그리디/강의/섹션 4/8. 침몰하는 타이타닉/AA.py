import sys
sys.stdin = open('./그리디/강의/섹션 4/8. 침몰하는 타이타닉/타이타닉.txt','r')

re, boat = map(int, input().split()  ) 
member = list( map(int, input().split()) )
print(member)
member.sort()
# print(re, boat)
print(member)

cnt = 0 # 보트의 개수
total = 0
while member: # 사람들이 다 빠져나갈 때까지 반복문을 수행한다. # 한 보트에 최대 2명까지만 태울 수 있다.
    if len(member) ==1:                 # 한 명만 남게되면 자기 자신을 두 번 더하게 된다. 문제가 발생한다.
        cnt+=1
        break
    if member[0] + member[-1] > boat:   # 둘을 함께 태우지는 못하는 상황을 말한다.                               
        member.pop()                    # 가장 무거운 사람을 보트에 태운다.
        cnt += 1
    else:
        member.pop(0)
        member.pop()
        cnt+=1
print(cnt)