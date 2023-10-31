import sys;input=sys.stdin.readline
A = str(input().rstrip())
B = str(input().rstrip())

cnt = 0
for i in A:
    if i in B:
        cnt += 1
        print(B.index(i))

# print(cnt)
