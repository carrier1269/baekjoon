import sys; input=sys.stdin.readline
n = int(input());temp_list=[]
for _ in range(n):
    y, x = map(int, input().split())
    temp_list.append([x,y])

for i, j in sorted(temp_list):
    print(j, i)