import sys;input=sys.stdin.readline
from collections import deque
N=int(input()); stack = deque()
for _ in range(N):
    ip = str(input().rstrip())

    if ip[:4] == "push":
        _, B = map(str,ip.split())
        stack.append(B)
    else:
        A = ip
        if A == "pop":
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        elif A == "size":
            print(len(stack))
        elif A == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif A == "front":
            if stack:
                print(stack[0])
            else:
                print(-1)
        elif A == "back":
            if stack:
                print(stack[-1])
            else:
                print(-1)