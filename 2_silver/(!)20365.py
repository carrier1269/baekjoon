import sys;input=sys.stdin.readline
from collections import Counter
n = int(input())
s = str(input().rstrip())

ct = Counter(s)

state = False

if ct['B'] > ct['R']:
    if s[0] == 'R':
        cnt = 0
    else:
        cnt = 1
    for i in range(n):
        if s[i] == 'R':
            if state == True:
                continue
            else:
                cnt += 1
            state = True
        else:
            state = False
elif ct['B'] == ct['R']:
    cnt = 1
    start = s[0]

    for x in range(n):
        if s[x] != start:
            if state == True:
                continue
            else:
                cnt += 1
            state = True
        else:
            state = False
else:
    if s[0] == 'B':
        cnt = 0
    else:
        cnt = 1
    for j in range(n):
        if s[j] == 'B':
            if state == True:
                continue
            else:
                cnt += 1
            state = True
        else:
            state = False

print(cnt)
