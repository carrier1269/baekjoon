import sys;input=sys.stdin.readline
white_cnt = 0

for i in range(1, 9):
    chess = list(str(input().rstrip()))

    if i % 2 == 0:
        for x in range(1, 8, 2):
            try:
                if chess[x] == 'F':
                    white_cnt += 1
            except:
                continue
    else:
        for y in range(0, 8, 2):
            try:
                if chess[y] == 'F':
                    white_cnt += 1
            except:
                continue
print(white_cnt)