import sys
sys.stdin = open("input.txt", "r")

def bfs(a, b):
    q= []
    
    q.append((a, b)) # 현재 단지의 주소를 넣어두기
    visit[a][b] = 1 # 먼저 나중에 다시 돌아오지 않도록 방문 표시를 하자
    cnt = 1 # 집 숫자
    
    while q: # 밑에 문장을 반복하기 위해 사용
        ca, cb = q.pop(0) # 밑에 for에서 체크된 주소에 따라 차례대로 상하좌우 돌기 위해 pop 사용.
        for da, db in ((-1,0), (1,0), (0,-1), (0,1)  ): # 상, 하, 좌, 우 # direction a, b # 행이 작아지면 윗칸, 열이 작아지면 좌측
                na, nb = ca+da, cb+db # 단지에서 1 더하고 뺴며 상하좌우 돌아다니기 # next a, b
                if (0<= na <n) and (0 <= nb < n) and (visit[na][nb]==0) and (house[na][nb] ==1): # 돌아다닌다, 앞에 2개는 범위 지정, 방문 X, 단지 존재
                    q.append((na, nb)) # 단지를 넣는다. # 방문한 곳 제외 나머지 주변값들이 0이라면 더 이상 실행 X
                    visit[na][nb]=1 # 방문 표시하기. 예시, 1행 2열은 방문했다, 2행 3열은 방문했다. 1 표시하고 나중에 재방문 X
                    cnt += 1 # 인접한 집 하나 추가
    return cnt
                
n = int(input()) # 정사각형 지도 가로 세로 크기 정의

house = [list( map( int, input() ) ) for _ in range(n) ] # 정사각형 지도 만들기
           
visit = [[0]*n for _ in range(n)] # 방문 여부 표시 공간 0으로 채워서 똑같은 크기로 만들기

ans = [] # 정답 공간

for i in range(n): # 정사각형 지도를 돌아다니며 체크하자 # 사각형 돌아다니기 위해 for문 2번 사용
    for j in range(n):
        if house[i][j] == 1 and visit[i][j]==0: # 지도에 주택이 있는데, 방문 표시를 하지 않았다.
            ans.append(bfs(i,j)) # 정답 칸에 bfs 홤수에 따라 단지 숫자를 채운다.

ans.sort() # 문제 조건에서 오름차순

print(len(ans), *ans, sep='\n') # len(ans)는 연결된 집 숫자, ans를 unpacking하면서 하나씩 출력