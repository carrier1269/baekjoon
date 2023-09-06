import sys

def input():
    return sys.stdin.readline()

h, m = map(int, input().split())

plus_time = int(input())

time = h * 60 + m

time += plus_time

fin_h = time // 60

fin_m = time % 60

if fin_h >= 24:
    fin_h -= 24

print(f'{fin_h} {fin_m}')