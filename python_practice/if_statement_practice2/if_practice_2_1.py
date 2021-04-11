# 2.2 if_statement_practice 문제 1

num = int(input("입력하시오: "))

if num % 3 == 0 and num % 5 ==0:
    print('"FizzBuzz"')
elif num % 3 == 0:
    print('"Fizz"')
elif num % 5 == 0:
    print('"Buzz"')
