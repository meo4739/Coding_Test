import sys
sys.stdin = open("./DFS, BFS/백준_스터디/29(일)/number_island.txt", "r")


def bfs(a, b):
    q= []
    
    q.append((a, b)) # 현재 단지의 주소를 넣어두기
    chk[a][b] = 1 # 먼저 나중에 다시 돌아오지 않도록 방문 표시를 하자
    cnt = 1 # 집 숫자
    
    while q: # 밑에 문장을 반복하기 위해 사용
        ca, cb = q.pop(0) # 밑에 for에서 체크된 주소에 따라 차례대로 상하좌우 돌기 위해 pop 사용.
        print(f"ca, cb : {ca} {cb}")
        for da, db in ((-1,0), (1,0), (0,-1), (0,1), (1,1), (1,-1), (-1,1),(-1,1)  ): # 상, 하, 좌, 우 # direction a, b # 행이 작아지면 윗칸, 열이 작아지면 좌측
                na, nb = ca+da, cb+db # 단지에서 1 더하고 뺴며 상하좌우 돌아다니기 # next a, b
                if (0<= na <width) and (0 <= nb < height) and (chk[na][nb]==0) and (space[na][nb] ==1): # 돌아다닌다, 앞에 2개는 범위 지정, 방문 X, 단지 존재
                    q.append((na, nb)) # 단지를 넣는다. # 방문한 곳 제외 나머지 주변값들이 0이라면 더 이상 실행 X
                    chk[na][nb]=1 # 방문 표시하기. 예시, 1행 2열은 방문했다, 2행 3열은 방문했다. 1 표시하고 나중에 재방문 X
                    cnt += 1 # 인접한 집 하나 추가
    return cnt


while True: # 마지막 줄에 0, 0이 입력되기 전까지는 계속하여 입력받자.

    width, height = map(int, input().split()) # 사각형의 크기를 정한다.

    space = [] # 지도 그리기

    n = width * height # 지도 크기를 뜻한다.

    for _ in range(height):
        space.append( list(map(int, input().split() ) ) )
    
    chk = [[0]  * width for i in range(height)]
    
    if width ==0 & height ==0: # 마지막 줄에는 0 0이 입력된다. 그 떄 멈춘다.
        break

    print(bfs(width, height)  )
