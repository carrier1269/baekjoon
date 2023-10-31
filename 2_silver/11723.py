import sys;input=sys.stdin.readline

M = int(input())

rs = []

for _ in range(M):
    ins = input().rstrip()

    if str(ins[:3]) == 'all':
        rs = [i for i in range(1, 21)]
        continue
    elif str(ins[:5]) == 'empty':
        rs.clear()
        continue
    else:
        a, b = map(str, ins.split())

        b = int(b)

        if a == 'add':
            if b in rs:
                continue
            rs.append(b)
        elif a == 'remove':
            if b not in rs:
                continue
            rs.remove(b)
        elif a == 'check':
            if b in rs:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if b in rs:
                rs.remove(b)
            else:
                rs.append(b)