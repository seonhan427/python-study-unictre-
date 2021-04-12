# practice loop 1 문제4

while True:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    number = int(input("number?"))
    
    if number == 1:
        print("Seoul")
        continue
    elif number == 2:
        print("Washington")
        continue
    elif number == 3:
        print("Tokyo")
        continue
    elif number == 4:
        print("Beijing")
        continue
    else:
        print("none")
        break