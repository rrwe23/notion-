#아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

number_list = [1, 23, 9, 6, 91, 59, 29]
number = max(number_list)


number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
number2 = max(number_list2)


if number > number2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif number < number2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


# 예약어(max)를 변수명으로 사용했기 때문에 생기는 오류이며 변수명을 다른 것으로 변경해주면 오류가 사라진다.
