import sys
n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack.append(int(sys.stdin.readline()))
stack.sort(reverse=True)
ans = 0
for i in range(0,len(stack)):
    if (stack[i] - i) > 0:
        ans += (stack[i] - i)
    else:
        break
print(ans)
