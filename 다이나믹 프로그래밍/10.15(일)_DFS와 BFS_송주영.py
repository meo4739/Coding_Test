# 입력 받기
N, V, M = map( int, input().split())

# 그래프 & 방문 횟수 기록 칸 만들기
graph = [[False] * (N+1) for i in range(N+1) ] 
visited = [False] * (N+1)

# for 그래프에 방문 정보 입력
for _ in range(M):
    a, b = map( int, input().split())
    
    # 양방향 연결
    graph[a][b] = True
    graph[b][a] = True
    
# dfs

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

# V는 첫 번째 방문 노드

# dfs

def dfs(idx):
    global visited
    # 시작 노트 V는 방문했다 표시
    visited[idx] = True
    print(idx, end = ' ')
    
    # 1 ~ 4 정점에 대해 확인
    for next in range(1, N+1):
        
        if not visited[next] and graph[idx][next]:
        
            dfs(next)
     
dfs(V)

print()       

# bfs

# 초기화
visted = [Flase] * (N+1)
q = [V]
visited[V]= True


def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
                
                
                
bfs(V)