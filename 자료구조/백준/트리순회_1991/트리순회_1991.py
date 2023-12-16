import sys
sys.stdin = open('./자료구조/백준/트리순회_1991.txt')
input = sys.stdin.readline

nodes = []

for i in range(int(input())):
    nodes.append( list(input().split()) )

print(nodes)

for node, left, right in nodes:
    print(node, left, right)