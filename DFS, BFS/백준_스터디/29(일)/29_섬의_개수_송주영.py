import sys
sys.stdin = open("./DFS, BFS/백준_스터디/29(일)/number_island.txt", "r")

dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1) ] # 위에서부터 시계 방향으로 탐색한다.

def numland(width, height, space):
    cnt = 0 # 섬 숫자
    
    for i in range(height): # 지도를 탐색한다.
        for j in range(width):
            if space[i][j] == 1:
                cnt +=1 # 섬이 있으면 count를 더하고 주변을 탐색한다.
                check(space, i, j)
    return cnt

def check(space,i ,j): # 방문하면 주변의 연결된 땅을 모두 0으로 바꿔 다음에 방문하지 않도록 한다.
    if space[i][j] == 0: # 1 표시가 없다면 호출된 재귀함수를 종료한다.
        return
        
    space[i][j] = 0  # 방문하였다면 표시를 0으로 바꾸어 둔다. 연결된 1은 다 0이 될 때까지 밑에 반복문 실행

    for d in dir: # 위에서 정한 방향대로 탐색한다.
        ny = i + d[0] # height는 행과 같다.
        nx = j + d[1] # width 는 열과 같다.
        if ny < 0 or nx < 0 or nx >= width or ny >= height: # 범위를 벗어난 경우를 말한다.
            continue
        if space[ny][nx] == 1:
            check(space, ny, nx)
            

while True: # 마지막 줄에 0, 0이 입력되기 전까지는 계속하여 입력받자.

    width, height = map(int, input().split()) # 사각형의 크기를 정한다.
    # print(f"width : {width}, height : {height}")

    if width ==0 and height ==0: # 문제에서 마지막 줄에는 0 0을 입력하고 종료한다.
        break

    space = [ list(map(int, input().split()) ) for _ in range(height) ] # 지도 그리기
    # space = [] 
    # for _ in range(height):
    #     space.append( list(map(int, input().split() ) ) )
    
    print(numland(width, height, space))
