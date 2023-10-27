import sys
sys.stdin = open("input.txt", "r")

while True: # 마지막 줄에 0, 0이 입력되기 전까지는 계속하여 입력받자.

    width, height = map(int, input().split()) # 사각형의 크기를 정한다.

    space = [] # 지도의 크기

    for _ in range(height):
        space.append( list(map(int, input().split() ) ) )
    
    chk = [[0]  * width for i in range(height)]
    
    print("space\n", space) # 지도의 크기
    print("chk\n",chk) # 방문 여부 체크
    
    
    if width ==0 & height ==0: # 마지막 줄에는 0 0이 입력된다. 그 떄 멈춘다.
        break