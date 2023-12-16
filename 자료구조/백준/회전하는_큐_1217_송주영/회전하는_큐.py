# import os
# print(os.getcwd())
# print(os.listdir())

import sys
sys.stdin = open('./자료구조/백준/회전하는_큐_1217_송주영/회전하는_큐_4.txt')
input = sys.stdin.readline

from collections import deque

numbers_len, rep = map(int, input().split())
numbers = deque([i+1 for i in range(numbers_len)])
members = deque(list( map(int, input().split()) ))

print('numbers', numbers)
print('members', members)
print('members[0]', members[0])
print('len(members)', len(members))

cnt = 0

print('='*50)
while True:
    print('='*50)
    print('members', members)
    print('numbers', numbers)
    if members[0] == numbers[0]:
        print('원하는 숫자를 추출한다.')
        members.popleft()
        numbers.popleft()
        print('len(members)', len(members))
        print('members', members)
        print('numbers', numbers)
        if len(members) ==0:
            break
    else:
        # 중앙보다 뒤에 위치하고 있으므로 큐를 오른쪽으로 밀면서 원하는 숫자가 뒤로 빠져나오도록 한다.
        if numbers.index(members[0]) > len(numbers)/2:
            print('큐를 오른쪽으로 민다.')
            print('before', numbers)
            numbers.appendleft(numbers[-1])
            numbers.pop()
            print('after', numbers)
            cnt+=1
        else:
        # 중앙보다 앞에 위치하고 있으므로 큐를 왼쪽으로 밀면서 원하는 숫자가 앞으로 위치하도록 한다.
            print('큐를 왼쪽으로 민다.')
            print('before', numbers)
            numbers.append(numbers[0])
            numbers.popleft()
            print('after', numbers)
            cnt+=1

print(cnt)