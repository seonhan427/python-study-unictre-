# practice loop 1 문제5

evencount=0
oddcount=0
number = 1

while number != 0:
    number = int(input("입력하시오 : "))
    if number == 0:
        break
    elif number % 2 != 0:
        oddcount +=1
    elif number % 2 == 0:
        evencount += 1
print("odd :",oddcount,"even :",evencount)
