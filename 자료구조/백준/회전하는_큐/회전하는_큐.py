import os
print(os.getcwd())
print(os.listdir())

import sys
sys.stdin = open('./자료구조/백준/회전하는_큐/회전하는_큐.txt')
input = sys.stdin.readline
print(input().split())

from collections import deque
deq = deque()

cnt = 0



