import sys; input=sys.stdin.readline ; garosu = []
n=int(input())
for i in range(n):
    a = int(input())
    if i == 1:
        a != 1
        garosu.append(0)
    garosu.append(a)
garosu.sort()
ls = []
for i in range(n):
    try:
        ls.append(garosu[i + 1] - garosu[i])
    except:
        continue

print(f'garo = {garosu}')

min_length= min(ls)

print(min_length)
if garosu[0] != 0:
    print(((max(garosu)-min(garosu))//min_length+1)-n)
else:
    print(((max(garosu)-min(garosu))//min_length+1)-n-1)


