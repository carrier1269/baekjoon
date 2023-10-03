import sys;input=sys.stdin.readline
n,m = map(int, input().split())
hear_set=set(str(input().rstrip()) for _ in range(n))
look_set=set(str(input().rstrip()) for _ in range(m))
rs=hear_set.intersection(look_set)
print(len(rs))
rs_list = sorted(list(rs))
for i in rs_list:
    print(i)