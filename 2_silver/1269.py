import sys;input=sys.stdin.readline;n,m=map(int,input().split())
a_set=set(map(int,input().split()));b_set=set(map(int,input().split()))
print(len(a_set.difference(b_set).union(b_set.difference(a_set))))