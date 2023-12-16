import sys
from collections import deque
sys.stdin = open('./자료구조/백준/큐.txt')
input = sys.stdin.readline

space = deque([])
for i in range(int(input())):
    a = input().strip()

    if len(a)==3:
        if space:
            print(int(space.popleft()))
        else:
            print(-1)
    
    elif len(a)==4:
        if a =='back':
            if space:
                print(int(space[-1]))
            else:
                print(-1)
        else:
            print(len(space))
    
    elif len(a)==5:
        if a == 'front':
            if space:
                print(int(space[0]))
            else:
                print(-1)
        else:
            if space:
                print(0)
            else:
                print(1)
    
    else:
        p, num = a.split()
        space.append(num)
