import sys;input=sys.stdin.readline
n=int(input());temp_list=[]
for _ in range(n):
    a = str(input().rstrip())
    if len(a) > 1:
        b, c = map(str, a.split())
        temp_list.append(c)
    else:
        a = int(a)
        if a == 2:
            try:
                print(temp_list.pop())
            except:
                print(-1)
        elif a == 3:
            print(len(temp_list))
        elif a == 4:
            if len(temp_list) == 0:
                print(1)
            else:
                print(0)
        elif a == 5:
            try:
                print(temp_list[-1])
            except:
                print(-1)