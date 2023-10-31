import sys;input=sys.stdin.readline
N, M = map(int,input().split())

from itertools import combinations

dont = set()

for _ in range(M):
    a = ''.join(map(str,input().split()))
    dont.add(a)

cnt = 0

for i in combinations([i for i in range(1, N+1)], 3):
    
    state = True

    for x in dont:
        if ''.join(map(str, i)).find(x) != :
            state = False 
            break
            

    if state == False:
        continue
    else:
        cnt += 1

print(cnt)
