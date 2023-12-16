# import os
# print(os.getcwd())
# print(os.listdir())

import sys
sys.stdin = open('./자료구조/백준/회전하는_큐/회전하는_큐.txt')
input = sys.stdin.readline

from collections import deque

numbers_len, rep = map(int, input().split())
numbers = deque([i+1 for i in range(numbers_len+1)])
members = list( map(int, input().split()) )

print(members)

cnt = 0

while cnt<3:
    
    if members[0] == numbers[0]:
        members.popleft()
        numbers.popleft()
        print(members)
        print(numbers)

    else:
        # 중앙보다 뒤에 위치하고 있으므로 큐를 오른쪽으로 밀면서 원하는 숫자가 뒤로 빠져나오도록 한다.
        if numbers.index(members[0]) > numbers.index()/2:
            members.appendleft()
            print(members)
            print(numbers)
            cnt+=1
        else:
        # 중앙보다 앞에 위치하고 있으므로 큐를 왼쪽으로 밀면서 원하는 숫자가 앞으로 위치하도록 한다.
            print(members)
            print(numbers)
            cnt+=1