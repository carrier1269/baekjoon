import sys

def input():
    return sys.stdin.readline()

sum_price = int(input())

check_sum_price = 0

for _ in range(int(input())):
    price, count = map(int, input().split())

    check_sum_price += price * count

if check_sum_price == sum_price:
    print("Yes")
else:
    print("No")