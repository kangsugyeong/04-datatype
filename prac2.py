# text = input("메시지를 입력하세요.:")
# a = len(text)
# if a <= 20 :
#     print("50원")
# else :
#     print("100원")

# score = int(input("점수를 입력하세요.:"))
# if 81 <= score <= 100 :
#     print("A")
# elif 61 <= score <= 80 :
#     print("B")
# elif 41 <= score <= 60 :
#     print("C")
# elif 21 <= score <= 60:
#     print("D")
# elif 0 <= score <= 20 :
#     print("E")

num = int(input("숫자를 입력하세요.:"))
a = num % 2
if a == 0 :
    print("짝수")
elif a != 0 :
    print("홀수")