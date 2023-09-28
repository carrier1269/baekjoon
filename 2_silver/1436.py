def find_number(n):
    cnt, number = 0, 0
    while cnt < n:
        number += 1
        temp = str(number)
        if '666' in temp:
            cnt += 1
    return int(temp)

print(find_number(int(input())))