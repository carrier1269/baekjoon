import sys;input=sys.stdin.readline
n, m = map(int,input().split());d={}
for _ in range(n):
    a = str(input().rstrip())

    if len(a) >= m:
        try:
            d[a][0] += 1
        except:
            d[a] = [1, len(a), a]

t = sorted(d.values(), key= lambda x : (-x[0], -x[1], x[2]))

for i in t:
    print(i[2])