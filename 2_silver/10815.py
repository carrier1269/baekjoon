import sys;input=sys.stdin.readline
n=int(input());temp_list=set(map(int,input().split()))
m=int(input());check_list=list(map(int,input().split()));result=[]
print(*[1 if i in temp_list else 0 for i in check_list])