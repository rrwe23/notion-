#두 수를 Input으로 받아 합을 구하는 코드이다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

numbers = map(int,input().split())

print(sum(numbers))


# numbers 를 리스트(str)로 작성하고 sum을 하여 오류가 생겼다. 이를 위해 list를 map을 통해 입력받는 항목을 int로 통일
# 하여 받아 sum을 하였다.

