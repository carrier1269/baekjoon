import sys

input = sys.stdin.readline # 입력받는 속도를 더 향상시키기 위해서 사용한다.

n = int(input()) # 하나의 수를 입력받는다

t = list(map(int, input().split(" "))) # 3 1 4 3 2의 같은 형태를 입력받아 하나의 리스트에 저장한다.

t.sort() # t list값들을 오름차순으로 정렬한다.

time = 0

for x in range(1, n+1):
    time += sum(t[0:x]) # t 리스트의 0부터 자기의 순번까지 모두 더하는것을 time값에 더해준다.
    
print(time)
