import sys;input=sys.stdin.readline
N=int(input()); stack = []
for _ in range(N):
    ip = str(input().rstrip())

    if ip[:4] == "push":
        _, B = map(str,ip.split())
        stack.append(B)
    else:
        A = ip
        if A == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif A == "size":
            print(len(stack))
        elif A == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif A == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)