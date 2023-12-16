import sys
sys.stdin = open('./자료구조/백준/트리.txt')
input = sys.stdin.readline

# 1] 노드 개수를 입력 받는다
n = int(input())

# 2] tree 구조 및 방문 여부 표시를 리스트를 만든다.
tree = [[] for _ in range(n)]
visited = [False] * n

# 3] 부모 노드, answr를 0으로 초기화하여 선언한다.
root = 0
answer = 0

# 4] 부모의 경우 -1이므로, 이때 노드 값을 root 값에 대입한다.
for node, parent in enumerate(map(int, input().split())):
    print(node,parent)
    if parent == -1:
        root = node
    else:
        tree[parent].append(node)
print('root',root)
print('tree', tree)

# 5] 삭제할 노드를 입력 받고, 삭제할 부분은 방문 여부를 True로 표시한다.
deleted = int(input())
visited[deleted] = True
print('deleted', deleted)
print('visited', visited)

# 6] dfs를 수행하며, visited가 true이면 함수 종료
def dfs(s):
    global answer

    if visited[s]: return
    visited[s] = True
    print('s',s)
    print('len', len(tree[s]))

    if len(tree[s]) == 0:
        answer += 1
        return
    elif len(tree[s]) == 1 and tree[s][0] == deleted:
        answer += 1

    
    for x in tree[s]:
        dfs(x)

dfs(root)
print(answer)