# 2.2 if_statement_practice 문제 7

A, B = input("가위바위보를 입력하시오: ").split()

if A =="가위":
    if B == "가위":
        print("무승부입니다.")
    elif B == "바위":
        print("B가 이겼습니다.")
    elif B == "보":
        print("A가 이겼습니다.")
elif A == "바위":
    if B == "가위":
        print("A가 이겼습니다.")
    elif B == "바위":
        print("무승부입니다.")
    elif B == "보":
        print("B가 이겼습니다.")
elif A == "보":
    if B == "가위":
        print("B가 이겼습니다.")
    elif B == "바위":
        print("A가 이겼습니다.")
    elif B == "보":
        print("무승부입니다.")