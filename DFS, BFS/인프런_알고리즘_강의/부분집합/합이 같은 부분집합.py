import sys
sys.stdin = open('DFS, BFS\인프런_알고리즘_강의\부분집합\합이 같은 부분 집합.txt','r')



n = int(input()) # 성분의 개수를 입력하자
a = list(map( int, input().split() )) # 안에 있는 요소들을 출력하자.
total = sum(a)
DFS(0, 0) # 여기에서 앞에 0은 시작 지점, 뒤에 옆은 현재까지의 누적합을 의미한다.

# print(int(input())) # 입력이 똑바로 되어있는지 확인하자
# print( list(map( int, input().split()))) # 입력이 똑바로 되어있는지 확인하자

