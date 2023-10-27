import sys
sys.stdin = open("input.txt", "r")

def bfs(a, b):
    q = [] # 
    
    q.append((a,b)) # 주소 담기
    visit[a][b] = 1 # 방문 완료
    cnt = 1 # 밭 1개
    
    while q: # 밑에 for문 반복
        ca, cb = q.pop(0)# check할 좌표 a, b 밑에서 추가하고 차례대로 빼면서 확인
        print(f"ca : {ca} cb : {cb} 체크 포인트")
        for da, db in ((-1,0), (1,0), (0,-1), (0,1)):
            na, nb = ca+da, cb+db
            print(f"na : {na} nb : {nb} 방문")
            if (0<= na <length) & (0<= nb < width) & ( visit[na][nb]==0) & (space[na][nb]==1):
                q.append((na, nb))
                visit[na][nb]=1
                cnt+=1
        print(q)
    return cnt

case = int(input()) # 테스트 케이스

for test in range(case): # 테스트 케이스 갯수 만큼 반복
    print("테스트 시작")
    width, length, number= map(int, input().split()) # 가로, 세로, 갯수
    
    space = [[0] * width for _ in range(length)] # 밭의 크기
    space = # space에 배추 심기
    
    visit = [[0]* width for _ in range(length)] # 방문 체크
    ans = [] # 정답 담기
    
    
    
    for i in range(length): # 사각형 돌아다니기 => for문 두 개, 1행부터 차례대로
        for j in range(width): # 사각형 돌아다니기 => 오른쪽으로 쭉
            if space[i][j] == 1 & visit[i][j] ==0: # 배추는 있는데 방문 X
                ans.append(bfs(i,j)) # bfs로 상하좌우 돌아다니기
        
    

    

# for i in range(number): # 테스트 케이스 만큼 반복문 시작
#     p1, p2 = map(int, input().split()) # 좌표 찍기
