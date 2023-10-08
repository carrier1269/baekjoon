import sys;input=sys.stdin.readline
from collections import deque
n=int(input()); t = deque()
for _ in range(n):
    a = str(input().rstrip())

    if a[0:4] == "push":
        b, c = a.split()

        t.append(c)
    else:
        if a == "pop":
            if t:
                print(t.popleft())
            else:
                print(-1)
        elif a == "size":
            print(len(t))
        elif a == "empty":
            if t:
                print(0)
            else:
                print(1)
        elif a == "front":
            if t:
                print(t[0])
            else:
                print(-1)
        elif a == "back":
            if t:
                print(t[-1])
            else:
                print(-1)