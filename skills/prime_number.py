# 거의 모든 문제에 hidden case, 반례로 1이 들어간다.
# 1은 소수가 아님을 명시해야 한다.

n=int(input())

# 나누는 범위를 n까지 하면 최악의 경우 O(n)의 시간 복잡도가 발생
# int(n**0.5)+1로 설정하여 중간에 결과를 반환

st = True

for i in range(2, int(n**0.5)+1):
    

    if n % i == 0:
        st = False
        
if st != False:
    print(f'n == 소수')
else:
    print(f'n == 소수가 아님')

# 더 빠른 소수 생성기

# K는 자리수

K = int(input())

is_prime = [True] * (10**K)

iter_range = int((10**K)**0.5)
for i in range(2, iter_range + 1):
    if is_prime[i]:
        for j in range(i+i, 10**K, i):
            is_prime[j] = False