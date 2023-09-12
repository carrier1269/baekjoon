import sys

input = sys.stdin.readline

n = int(input())

string = ""

for _ in range(n):
    r, s = map(str, input().rstrip().split())

    r = int(r)

    for a in s:
        string += a * r

    print(string)

    string = ""