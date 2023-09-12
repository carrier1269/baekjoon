import sys

input = sys.stdin.readline

string_list = list(map(str, input().rstrip().split()))

print(len(string_list))