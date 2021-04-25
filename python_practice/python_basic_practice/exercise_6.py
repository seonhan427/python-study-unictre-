# python basic practice 문제 6

#입력값을 여러번 받기위해서 for문을 사용했습니다
letterlist = []
for x in range(10):
    letterlist.append(input("입력하시오: "))
key = input("문자하나를 입력하시오: ") #키값을 받기위한 input

# 키값으로 끝나는 단어를 찾아서 분류하기위해 for문 사용했습니다
awnser = []
for x in letterlist:
    if x.endswith(key):
        awnser.append(x)
print(awnser)