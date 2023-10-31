import sys;input=sys.stdin.readline
account = int(input())
worth = list(map(int,input().split()))

SUNGMIN = account
JUNHYUN = account

for i in worth:
    if JUNHYUN >= i:
        JUNHYUN = JUNHYUN // i
    
JUNHYUN = JUNHYUN * worth[-1]

start_worth = worth[0]

cnt1 = 0
cnt2 = 0

coin = 0

state = False

for j in range(1, len(worth)):
    if worth[j] < start_worth:
        cnt2 = 0
        start_worth = worth[j]
        cnt1 += 1

        if SUNGMIN >= worth[j] and cnt1 == 3:
            cnt1 = 0
            coin = SUNGMIN // worth[j]
            SUNGMIN = SUNGMIN - coin * worth[j]
            state = True
    elif worth[j] == start_worth:
        if SUNGMIN >= worth[j] and SUNGMIN != 0:
            coin += SUNGMIN // worth[j]
            SUNGMIN -= SUNGMIN // worth[j] * worth[j]
            state = True
    else:
        cnt1 = 0
        start_worth = worth[j]
        cnt2 += 1

        if cnt2 == 3:
            cnt2 = 0
            SUNGMIN += coin * worth[j]
            state = False

if state:
    SUNGMIN = coin * worth[-1] + SUNGMIN
else:
    pass

if JUNHYUN > SUNGMIN:
    print('BNP')
elif JUNHYUN == SUNGMIN:
    print('SAMESAME')
else:
    print('TIMING')
