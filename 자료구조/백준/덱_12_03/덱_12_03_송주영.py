import sys
sys.stdin = open('./자료구조/백준/덱_12_03_송주영.txt')
input = sys.stdin.readline

from collections import deque
deq = deque()

for i in range(int(input())):
    n = input().split()

    if len(n) >=2:
        if n[0] =='push_front':
            deq.appendleft(n[1])
        else:
            deq.append(n[1])
    else:
        if n[0] == 'pop_front':
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        
        elif n[0] == 'pop_back':
            if deq:
                print(deq.pop())
            else:
                print(-1)

        elif n[0] == "size":
                print(len(deq))

        elif n[0] == "empty":
            if deq:
                print(0)
            else:
                print(1)


        elif n[0] == "front":
            if deq:
                print(deq[0])
            else:
                print(-1)

        elif n[0] == "back":
            if deq:
                print(deq[-1])
            else:
                print(-1)

    # else:

    
    # print(deque[1])

# print(deq)   

# print(deq[-1])
# print(len(deq))

