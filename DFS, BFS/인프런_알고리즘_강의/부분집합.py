import sys
sys.stdin = open("input.txt","r") # sys.stdin을 input.txt 파일로 재지정합니다. 따라서 이후에 input() 함수를 사용하면 터미널에서 입력을 받는 대신 input.txt 파일에서 입력을 받게 됩니다.

def DFS(v):
    if v == n+1: # v 값이 input 값인 n 보다  1 만큼 큰 경우를 말한다.
        for i in range(1, n+1):
            if ch[i] == 1: # 
                print(i, end = ' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]= 0
        DFS(v+1)

n = int(input())
ch = [0] *(n+1) # ch는 체크를 하는 공간으로서 인덱스를 편하게 사용하기 위하여 [0]을 (n+1)개 생성해준다.
DFS(1) 

# if __name__ =="__main__": # 이 조건문은 현재 스크립트가 직접 실행될 때만 아래의 코드 블록을 실행하라는 의미
#     n = int(input())
#     ch = [0] *(n+1) # 체크
#     DFS(1)
    
# 예를 들어, 이 스크립트를 다른 파이썬 파일에서 import하여 사용할 경우, 
# 이 조건문 아래의 코드는 실행되지 않습니다. 이는 모듈로써 사용될 때와 직접 실행될 때의 동작을 구분하기 위한 표준 Python 패턴입니다.
