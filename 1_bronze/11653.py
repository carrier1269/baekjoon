import sys

input = sys.stdin.readline

n = int(input())

# for i in range(2, n + 1):
#     while(True):
#         if n % i == 0:
#             n = n / i
#             print(i)
#         else:
#             break

for i in range(2, n + 1):
    def div():
        global n
        if n % i == 0:n = n / i;print(i);div()
        else:return
    div()