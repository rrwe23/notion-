#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
#양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

number = int(input())

cnt = 0

while number > 0:
    number //=10  
# '//=' 기존 왼쪽 변수 값과 오른쪽 변수로 나눈 후 내림한 값을 재할당
    cnt += 1

print(cnt)
