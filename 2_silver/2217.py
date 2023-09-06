import time


def solution(n, lost, reserve):
    lst = []
    
    for i in range(1, n+1):
        lst.append(i)
        
    print(lst)
    print(lost)
    print(reserve)
        
    for i in lost:
        for j in reserve:
            print(f'({i},{j})')
            
            print(f'i = {i} j = {j} lost = {lost} reserve = {reserve}')
            
            time.sleep(1)
            
            if i-1 or i+1 == j:
                # print(f'lost={lost}{i}reserve={reserve}{j}')
                if i not in lost:
                    continue
                else:
                    lost.remove(i), reserve.remove(j)
                # print(f'rmlost={lost}rmreserve={reserve}')

            
    print(f'lost 리스트는 {lost}')   
    
    return len(list(set(lst)-set(lost)))

print(solution(3, [3], [1]))