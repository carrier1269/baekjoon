import sys

input = sys.stdin.readline

chess_list = [1, 1, 2, 2, 2, 8]

a, b, c, d, e, f = map(int, input().split())

input_chess = [a, b, c, d, e, f]

fix_list = []

for i in range(len(input_chess)):
    fix_list.append(chess_list[i] - input_chess[i])

print(" ".join(map(str, fix_list)))