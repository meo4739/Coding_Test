import sys
import heapq as hq
sys.stdin = open("./자료구조/강의/섹션 5/11. 최대힙/input.txt","r")
a = []
while True:
    n = int(input())
    if n==1:
        break
    if n==0:
        if len(a) ==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)