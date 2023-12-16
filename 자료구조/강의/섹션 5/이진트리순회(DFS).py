import sys
sys.stdin = open('./자료구조/강의\섹션 5/이진트리순회(DFS).txt')
input = sys.stdin.readline

# ### 전위 순회
# def DFS(v): # 부모 노드
#     if v>7:
#         return
#     else:
#         print(v, end = ' ')
#         DFS(v*2) # 왼쪽 노드
#         DFS(v*2+1) # 왼쪽 자식노드

# ### 중위 순회
# def DFS(v): # 부모 노드
#     if v>7:
#         return
#     else:
#         DFS(v*2) # 왼쪽 노드
#         print(v, end = ' ')  #  DFS(2)  DFS(4)  
#         DFS(v*2+1) # 왼쪽 자식노드

### 후위 순회
def DFS(v): # 부모 노드
    if v>7:
        return
    else:
        
        DFS(v*2) # 왼쪽 노드
        DFS(v*2+1) # 왼쪽 자식노드
        print(v, end = ' ')

if __name__ == "__main__":
    DFS(1)
    