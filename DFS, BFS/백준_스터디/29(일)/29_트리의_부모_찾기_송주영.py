import sys
sys.stdin = open("./DFS, BFS/백준_스터디/29(일)/tree.txt", "r")

def DFS(x): # 루트인 1부터 시작한다.
    chk[x] = True # 처음에 1을 방문을 하였으니 체크하자.
    for i in connect[x]: # 처음 시작하는 connect[1] = [4,6]이다.
        if not chk[i]: # 방문한 적이 없는 노드에 도착
            ans[i] = x # 4의 부모 노드는 현재 x인 1이 된다.
            DFS(i) # 4에 대한 DFS가 시작한다.

n = int(input()) # 노드의 개수를 입력받자.
chk = [False] * (n+1) # 방문 여부를 체크하자. 노드는 1부터 시작한다.
connect = [[] for _ in range(n+1) ] # 연결 관계를 기록하자
ans = [0]*(n+1) # 부모 노드를 기록하자

for _ in range(1,n): # 반복문으로 연결관계를 채워나간다. 6개의 연결관계를 제시했다.
    p1, p2 = list(map( int, input().split() )) # 노드 2개 입력받기.
    connect[p1].append(p2) # 노드의 연결 관계 양방향으로 기록
    connect[p2].append(p1) # 노드의 연결 관계 양방향으로 기록

DFS(1) # 처음 루트가 1이다.

for i in range(2, n+1):
    print(ans[i])