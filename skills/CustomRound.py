def round_num(num):
    a = str(num).split('.')[1][0]

    if int(a) >= 5:
        return int(num) + 1
    else:
        return int(num)
    
# 파이썬의 경우 4.5인경우 4로 반올림한다.