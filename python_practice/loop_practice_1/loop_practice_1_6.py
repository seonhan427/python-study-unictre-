# practice loop 1 문제6

while True:
    base = int(input("Base ="))
    Height = int(input("Height ="))
    area = base*Height/2
    print("Triangle width =",area)
    anwser = input("continue?")
    if anwser == "Y"or anwser == "y":
        continue
    else:
        break
        
