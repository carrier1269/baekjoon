# 기존 dp 유형과 같이 리스트로 dp배열 생성시
# 인덱스 a,b,c 세개를 한번에 다룰수 없는 문제점이 발생해서
# 딕셔너리 key를 .기준으로 문자열 조합하여 dp생성

dp_dict = {}

def w(a, b, c):
    try:
        if dp_dict[str(a)+'.'+str(b)+'.'+str(c)]:
            return dp_dict[str(a)+'.'+str(b)+'.'+str(c)]
    except:
        if a <= 0 or b <= 0 or c <= 0: 
            dp_dict[str(a)+'.'+str(b)+'.'+str(c)] = 1
            return 1

        if a > 20 or b > 20 or c > 20: 
            dp_dict[str(a)+'.'+str(b)+'.'+str(c)] = w(20, 20, 20)
            return w(20, 20, 20)

        if a < b and b < c: 
            dp_dict[str(a)+'.'+str(b)+'.'+str(c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else: 
            dp_dict[str(a)+'.'+str(b)+'.'+str(c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)