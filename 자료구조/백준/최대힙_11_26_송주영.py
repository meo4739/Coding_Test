import sys
import heapq as hq
sys.stdin = open('./자료구조/백준/최대힙.txt')
input = sys.stdin.readline
a = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        if a:
            print(-hq.heappop(a))
        else:
            print(0)
    else:
        hq.heappush(a,-n)