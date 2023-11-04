import sys
sys.stdin = open('그리디\강의\회의실.txt','r')

cnt = 0
space = []

for i in range(int(input() )):
    a = list(map( int, input().split()))
    print(a)