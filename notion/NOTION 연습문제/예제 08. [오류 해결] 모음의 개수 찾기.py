# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)


word = "HappyHacking"


count = 0

for char in word:
    if char in ['a', 'e','i','o','u'] :
        count += 1
       
print(count)

# 리스트 []로 받아 == 가 아닌 in 으로 하여 리스트 안에서 검색하게 한다.

