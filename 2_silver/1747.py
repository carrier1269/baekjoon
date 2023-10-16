import sys;input=sys.stdin.readline
n=int(input())

def num_checker(num, i, j):
    if i >= len(num):
        return True
    if num[i] != num[j]:
        return False
    else:
        i += 1
        j -= 1
        return num_checker(num, i, j)
    
def prime_checker(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
    
while(True):
    if n == 1:
        n += 1
        continue
    
    prime_check = prime_checker(n)

    if prime_check:
        palindrome_check = num_checker(str(n), 0, len(str(n))-1)
        
        if palindrome_check:
            print(n)
            break
        else:
            n += 1
            continue

    else:
        n += 1
        continue