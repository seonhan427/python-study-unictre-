id_ilst = ["kim","yang","hong","lee"]

id_input = input("id를 입력하시오: ")

if id_input in id_ilst :
    password = int(input("비밀번호를 입력하시오: "))
    if password == 12345678 :
       print("환영합니다.")
    else :
        print("비밀번호가 일치하지 않습니다.")
else:
    print("등록되지 않은 ID입니다.")

