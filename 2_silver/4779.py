import sys;input=sys.stdin.readline

# 퀵 정렬을 튜닝해서 문자열 중앙 범위를 공백으로 만드는 재귀함수를 제작하였습니다.

def mid_blank(STRING):
    if len(STRING) <= 1:
        return STRING

    left, middle, right = '','',''

    for i in range(len(STRING)):
        if i < int(len(STRING)/3):
            left += STRING[i]
        elif i > int(len(STRING)/3*2-1):
            right += STRING[i]
        else:
            middle += " "

    return mid_blank(left) + middle + mid_blank(right)

while(True):
    try:
        n = int(input())
        tm = '-'*(3**n)
        print(tm)

        print(mid_blank(tm))
    except:
        break

# Short Version

# import sys;input=sys.stdin.readline
# def mid_blank(STRING):
#     if len(STRING)<=1:return STRING
#     left,middle,right ='','',''
#     for i in range(len(STRING)):
#         if i < int(len(STRING)/3):left += STRING[i]
#         elif i > int(len(STRING)/3*2-1):right += STRING[i]
#         else:middle += " "
#     return mid_blank(left)+middle+mid_blank(right)
# while(True):
#     try:print(mid_blank('-'*(3**int(input()))))
#     except:break