# n=int(input());s=set();count=0
# for _ in range(n):
#     a = str(input().rstrip())

#     if a == "ENTER":
#         count += len(s)
#         s=set()
#     else:
#         s.add(a)
# count += len(s)
# print(count)

n=int(input());s=set();count=0
for _ in range(n):
    a = str(input().rstrip())
    if a == "ENTER":count+=len(s);s=set()
    else:s.add(a)
print(count + len(s))
