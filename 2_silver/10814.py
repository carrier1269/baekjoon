import sys;input=sys.stdin.readline
n=int(input());temp_list=[[] for _ in range(201)]
for _ in range(n):
    age, name = map(str, input().rstrip().split())

    temp_list[int(age)].append(name)
for i in range(len(temp_list)):
    if temp_list[i] != 0:
        for j in range(len(temp_list[i])):
            print(i, temp_list[i][j])