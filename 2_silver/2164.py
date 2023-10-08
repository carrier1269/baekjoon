import sys;input=sys.stdin.readline
from collections import deque
n=int(input()); t=deque()
for i in range(1, n+1):
    t.append(i)
for _ in range(n):
    if len(t) == 1: break
    t.popleft()
    a = t[0]
    if len(t) > 1:
        t.remove(a);t.append(a)
    else:
        break
print(*t)