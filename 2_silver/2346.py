import sys;input=sys.stdin.readline
from collections import deque
n = int(input());rs,cnt=[], 1; state = False
t = deque(map(int, input().split()))
f = t.copy()
result = []

while(True):
    result.append(f.index(t.popleft())+1)
    if len(t) == 0:
        break

    if f[result[-1]-1] > 0:
        for _ in range(f[result[-1]-1]-1):
            t.append(t.popleft())
    else:
        for _ in range(-(f[result[-1]-1])):
            t.appendleft(t.pop())

print(*result)