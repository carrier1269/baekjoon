n = int(input())

def isPalindrome(STRING, i, r, cnt):
    if(i >= r): return 1, cnt
    elif STRING[i] != STRING[r]: return 0, cnt
    else:
        return isPalindrome(STRING, i+1, r-1, cnt+1)
for _ in range(n):
    st = str(input().rstrip())

    a, b = isPalindrome(st, 0, len(st)-1, 1)

    print(a, b)

# n = int(input())
# def P(S,i,r,cnt):
#     if(i>=r):return 1,cnt
#     elif S[i]!=S[r]: return 0,cnt
#     else:return P(S,i+1,r-1,cnt+1)
# for _ in range(n):
#     t=str(input().rstrip())
#     print(*P(t,0,len(t)-1,1))