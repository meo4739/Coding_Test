def DFS(v):
    global ans # DFS를 계속 실행할 거라 ans는 global로 정의해야 한다.
    
    ans += 1 # 방문했으니 +1
    chk[v] = 1 # 방문 체크
    
    for _ in connect[v]: # connect 안에는 숫자가 조합된 상태, v와 연결된 노드 처리
                         # 1에 연결된 것은 2와 5가 있고 2부터 순서대로 임무 시작
        if not chk[_]: # 방문을 하지 않았다면
            DFS(_)
        
n = int(input()) # 노드의 개수
m = int(input()) # 직접 연결된 갯수

connect = [[] for _ in range(n+1)] # n = 7일 경우, 0~7까지의 공간이 생기고 1~7 공간 활용
for _ in range(m): # 직접 연결된 조합을 connect 공간에 채우자
    p1, p2 = map( int, input().split())
    connect[p1].append(p2) # 연결 표시
    connect[p2].append(p1)
    
ans = 0
chk = [0] * (n+1)
DFS(1)
print(chk)
print(ans-1)