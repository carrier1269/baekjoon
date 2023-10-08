import sys;input=sys.stdin.readline
n=int(input())
for _ in range(n):
    st,a,k=str(input()),[],False
    for i in st:
        if i == "(":
            a.append(i)
        elif i == ")":
            if a:
                a.pop()
            else:
                k=True
                break
    if k == True:
        print("NO")
        continue
    if a:
        print("NO")
    else:
        print("YES")