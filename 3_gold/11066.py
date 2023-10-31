import sys;input=sys.stdin.readline




for _ in range(int(input())):
    N = int(input())

    num_list = list(map(int, input().split()))

    num_list.sort()

    sum = 0

    cnt_list = []

    print(num_list)

    def least_num_sum(number_list, i, j):
        global sum, cnt_list
        if i > j:
            return
        elif i == j:
            cnt_list.append(number_list[i])
        else:
            cnt_list.append(number_list[i] + number_list[j])
            return least_num_sum(number_list, i+1, j-1)
    

    least_num_sum(num_list, 0, len(num_list)-1)

    print(cnt_list)