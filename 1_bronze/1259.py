import sys;input=sys.stdin.readline
    
def is_pal(num, i, j):
    if i >= j:
        return True
    if num[i] != num[j]:
        return False
    else:
        return is_pal(num, i+1, j-1)
while(True):
    number = str(input().rstrip())

    if number == '0':
        break

    if is_pal(number, 0, len(number)-1):
        print('yes')
    else:
        print('no')