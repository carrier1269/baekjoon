state = 0

while(state <= 15):
    pixel = list(map(str, input().split()))

    for i in pixel:
        if i == 'w':
            print('chunbae')
            state += 15
            break
        elif i == 'b':
            print('nabi')
            state += 15
            break
        elif i == 'g':
            print('yeongcheol')
            state += 15
            break

    state += 1