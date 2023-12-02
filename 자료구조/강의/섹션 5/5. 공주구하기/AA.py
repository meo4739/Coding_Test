import sys
from collections import deque

sys.stdin = open('./자료구조/강의/섹션 5/5. 공주구하기/input.txt')
input = sys.stdin.readline

n, k = map(int, input().split())

dq = list(range(1, n+1))
# print(dq)
dq = deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) ==1:
        print(dq[0])
        dq.popleft()