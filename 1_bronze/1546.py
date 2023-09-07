import sys

input = sys.stdin.readline

n = int(input())

score_list = list(map(int, input().split()))

max_score = max(score_list)

for i in range(n):
    score_list[i] = score_list[i] / max_score * 100

sum_score = 0

average_score = 0

for a in score_list:
    sum_score += a

average_score = sum_score / n

print(average_score)