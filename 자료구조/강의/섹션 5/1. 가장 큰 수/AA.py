import sys
sys.stdin = open("./자료구조/강의/섹션 5/1. 가장 큰 수/in1.txt","rt")
num, m = map( int, input().split())
num = list(map( int, str(num) ))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]

for x in stack:
    print(x,end = '')