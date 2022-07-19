#정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 



n = int(input())

result = 0

while n > 0:  # 몫은 다음 number가 됨 나머지는 더해나가면 됨!
    #divmod(x,y) 는 x를 y로 나누고 결과를 tuple로 반환
    #(몫,나머지)
    result += n % 10
    n //= 10

print(result)