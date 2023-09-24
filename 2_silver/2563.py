import sys

input = sys.stdin.readline

n = int(input())

paper_list = []

color_paper_size = 10

for _ in range(100):
    paper_list.append([0] * 100)

temp_count = 0

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a - 1, a + color_paper_size - 1):
        for j in range(b - 1, b + color_paper_size - 1):
            paper_list[i][j] = 1

count = 0
for x in range(100):
    for y in range(100):
        if paper_list[x][y] == 1:
            count += 1

print(count)