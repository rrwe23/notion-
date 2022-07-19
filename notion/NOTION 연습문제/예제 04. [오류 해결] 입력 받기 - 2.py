#아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

# words = list(map(int, input().split()))
# print(words)


words = list(map(str, input().split()))
print(words)


# 문자열을 입력받는 상황에서 int로 입력받았기에 생기는 오류이다.
# int를 str로 수정해주었다.


