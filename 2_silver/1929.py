import sys;input=sys.stdin.readline
m, n = map(int,input().split())

def p(k):
    # 16인 경우 1, 2, 4, 8, 16이 있는데 소수가 아닐경우
    # 이미 int(16**0.5), 4까지 약수가 1을 제외하고
    # 2, 4가 있으므로 더 찾지 않고 소수가 아님을 판별
    for j in range(2,int(k**0.5)+1):
        if k % j == 0:
            return False
    return True
for i in range(m, n+1):
    if i == 1:
        continue
    if p(i):
        print(i)