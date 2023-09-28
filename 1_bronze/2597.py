# temp_list=[]
# for _ in range(5):
#     temp_list.append(int(input()))
# print(int(sum(temp_list)/len(temp_list)))
# print(temp_list[2])

temp_list=[]
for _ in range(5):temp_list.append(int(input()))
print("{}\n{}".format(int(sum(temp_list)/len(temp_list)),sorted(temp_list)[2]))