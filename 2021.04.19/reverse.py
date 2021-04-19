word = input("문자열을 입력하시오 : ")

reword = word[::-1]

if word == reword:
    print("회문입니다.")
else:
    print("회문이 아닙니다.") 