import sys
input = sys.stdin.readline

money = int(input())

coin = (5, 2)

count = 0

while True:
    if money % coin[0] == 0:
        count += money // coin[0]
        money = money % coin[0]
    
    else:
        money -= 2
        count += 1
        
    if money == 0:
        break
    
    if money < 0:
        break

if money < 0:
    print(-1)

else:
    print(count)