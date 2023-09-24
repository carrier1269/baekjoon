import sys

input = sys.stdin.readline

n = int(input())

temp_list = list(map(int, input().split()))

result_list = []

for i in temp_list:
    temp_number_list = []

    if i == 1:
        pass
    else:
        for j in range(2, i + 1):
            if i % j == 0:
                temp_number_list.append(j)
        if len(temp_number_list) == 1:
            result_list.append(*temp_number_list)
        else:
            pass
    
print(len(result_list))