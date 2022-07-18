# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

#answer = [] 를 통해 튜플(변경불가) 를 선언한 상태에서 append를 통한 수정이 불가능하기에 발생하는 오류이다.
# 변경가능한 리스트([])로 바꿔준다.