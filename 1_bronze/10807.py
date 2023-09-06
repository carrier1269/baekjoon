import sys

input = sys.stdin.readline

num = int(input())

lst = list(map(int, input().split()))

find_num = int(input())

print(lst.count(find_num))
