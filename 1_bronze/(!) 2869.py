import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())

day = 0
height = 0

while(True):
    day += 1

    height += a

    if height >= v:
        print(day)
        break
    else:
        height -= b