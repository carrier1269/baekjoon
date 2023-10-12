import sys;input=sys.stdin.readline
from collections import deque
n = int(input())
t = deque(enumerate(map(int, input().split())))
rs = []

while(True):
    rs.append(t[0][0] + 1)
    move = t.popleft()[1]

    if len(t) == 0:
        break

    if move > 0:
        for _ in range(move - 1):
            t.rotate(-1)
    if move == 0:
        continue
    if move < 0:
        for _ in range(-(move)):
            t.rotate(1)

print(*rs)
        
