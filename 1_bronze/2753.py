# import sys
# input = sys.stdin.readline()

# a = int(input)

# if a % 4 == 0 & a % 100 != 0:
#     print(1)
# elif a % 4 == 0 | a % 400 == 0:
#     print(1)
# else:
#     print(0)

# import sys
# input = sys.stdin.readline()

# a = int(input)

# if a % 4 == 0:
#     if a % 100 != 0:
#         print(1)
#     elif a % 400 == 0:
#         print(1)
# else:
#     print(0)

import sys
input = sys.stdin.readline()
a = int(input)

if a % 4 == 0 and a % 100 != 0:
    print(1)
elif a % 400 == 0:
    print(1)
else:
    print(0)