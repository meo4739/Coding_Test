import sys
sys.stdin = open('./자료구조/백준/스택_12_03_송주영.txt')
input = sys.stdin.readline

from collections import deque

def push(x):
    deq.append(x)

def pop():
    return deq.pop() if deq else -1

def size():
    return len(deq)

def empty():
    return 0 if deq else 1

def top():
    return deq[-1] if deq else -1

deq = deque()
commands = {
    'push' : push,
    'pop' : pop,
    'size' : size,
    'empty' : empty,
    'top' : top

}

for i in range(int(input())):
    command = input().split()
    # print(command)

    cmd = command[0]
    arg = command[1] if len(command) > 1 else None
    
    if cmd in commands:
        result = commands[cmd](arg) if arg is not None else commands[cmd]()
        if cmd != 'push':
            print(result)
