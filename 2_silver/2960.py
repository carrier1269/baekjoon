n, k = map(int,input().split())

lst = []
for i in range(2, n+1):
    lst.append(i)

cnt = 0

while(True):
    P = lst[0]

    del lst[0]

    cnt += 1

    if cnt == k:
        print(P)
        break

    for i in lst:
        if i % P == 0:
            lst.remove(i)
            cnt += 1

        if cnt == k:
            print(i)
            break

    if lst:
        pass
    else:
        break



  