# 이전 작성 코드인데, temp_list에 i를 검색하여, 최악의 시간복잡도에 의해 n^2 발생

# import sys;input=sys.stdin.readline
# from collections import Counter
# n=int(input())


# temp_list=list(map(int,input().split()))
# m=int(input());card_list=list(map(int,input().split()))
# rs = Counter(temp_list)
# rs_list = []
# for i in card_list:
#     if i in temp_list:
#         rs_list.append(rs[i])
#     else:
#         rs_list.append(0)

# print(*rs_list)

# try: except: 예외처리를 통해서 counter 라이브러리를 사용하여 원소를 검색후
# 예외 발생시 0을 추가하도록 수정

import sys;input=sys.stdin.readline
from collections import Counter
n=int(input())


temp_list=list(map(int,input().split()))
m=int(input());card_list=list(map(int,input().split()))
rs = Counter(temp_list)
rs_list = []
for i in card_list:
    try:
        rs_list.append(rs[i])
    except:
        rs_list.append(0)

print(*rs_list)