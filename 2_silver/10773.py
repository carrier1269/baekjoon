import sys;input=sys.stdin.readline
k=int(input());t=[]
for _ in range(k):
    a = int(input())
    if a == 0:t.pop()
    else:t.append(a)
print(sum(t))