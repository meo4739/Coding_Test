from collections import deque
a = deque([1,2,3])

print(a.pop())

print(a)

print(a.appendleft(a[-1]))

print(a)