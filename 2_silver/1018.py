import sys;input=sys.stdin.readline
n, m = map(int,input().split())

baduk_list = []
count_list = []

for _ in range(n):
    baduk_list.append(input().rstrip())

# 범위를 넘어가지 않기 위해 바둑판 8x8 범위의 시작점을 설정
for i in range(n-7):
    for j in range(m-7):
        w_count = 0
        h_count = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                # 2차원 배열의 인덱스를 2로 나눠 판별
                # 바둑 배열과 다를 경우 다른 카운트를 세도록 설정
                if (a+b)%2==0:
                    if baduk_list[a][b] == 'W':
                        w_count += 1
                    else:
                        h_count += 1
                else:
                    if baduk_list[a][b] == 'B':
                        w_count += 1
                    else:
                        h_count += 1
        count_list.append(w_count),count_list.append(h_count)

print(min(count_list))