import sys
sys.stdin = open('./자료구조/백준/덱_12_03_송주영.txt')
input = sys.stdin.readline

from collections import deque

def push_front(x):
    deq.appendleft(int(x))  # 입력값을 정수로 변환

def push_back(x):
    deq.append(int(x))  # 입력값을 정수로 변환

def pop_front():
    return deq.popleft() if deq else -1

def pop_back():
    return deq.pop() if deq else -1

def size():
    return len(deq)

def empty():
    return 0 if deq else 1

def front():
    return deq[0] if deq else -1

def back():
    return deq[-1] if deq else -1

deq = deque()
commands = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

for _ in range(int(input())):
    command = input().split()
    cmd = command[0]
    arg = command[1] if len(command) > 1 else None
    # print(cmd)

    if cmd in commands:
        result = commands[cmd](arg) if arg is not None else commands[cmd]()
        if cmd.startswith("pop") or cmd in ["front", "back","size","empty"]:
            print(result)
