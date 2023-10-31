import sys;input=sys.stdin.readline
A, B = map(str, input().split())

fi_sum = 0
for i in A:
    fi_sum += int(i)

sum = 0

for j in B:
    sum += fi_sum * int(j)

print(sum)