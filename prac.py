# 1. 사용자로부터 입력받아
# 2. 입력받은 값이 '안녕하세요'인 경우
# 3. 화면에 '반갑습니다'를 출력
#text = input('부디 안녕하세요 입력해주세요:')
#if text == "안녕하세요" :
#    print("반갑습니다.")

# 1. 사용자로부터 값 입력받아(문자열)
# 2. 입력받은 값에 100 더해(숫자형)
# 2-1. 입력받은 값에 100 더할 때 데이터 타입 변환 (문자열 -> 숫자형)
# 3. 더한 값이 150 초과인경우 사용자 입력값을 출력
# 4. 더한 값이 150 이하인경우 값이 부족합니다를 출력
#num = input("임의의 숫자를 입력하세요.:" )
#add = int(num) + 100
#if add > 150 :
#    print(num)
#elif add <= 150 :
#    print("값이 부족합니다.")

# num = int(input("값을 입력하세요: "))
# num = 6
# if 5 < num < 10 :
#    print("ok")
# elif num <= 5 :
#    print("no")
# else :
#    print("no")

# if 조회할 요소 in 조회할 대상(리스트, 딕셔너리 등)
# list = input("단어를 입력하세요.: ")
# fruit = ["사과", "포도", "홍시"]
# if list in fruit :
#     print("정답입니다.")
# else :
#     print("오답입니다.")

# text = input("단어를 입력하세요.: ")
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# if text in fruit:
#     print("정답입니다.")
# else :
#      print("오답입니다.")

text = input("메시지를 입력하세요.:")
if len(text) <= 20 :
    print("50원")
else :
    print("100원")