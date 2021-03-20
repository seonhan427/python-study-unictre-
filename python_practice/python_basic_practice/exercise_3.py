#python basic practice 문제 3

letter, number = input("입력하시오 : ").split(' ')
#number = int(input("숫자를 입력하시오 : "))

number1 = int(number)

letternumb = len(letter)
# lastletter = letternumb-letternumb*2
# number2 = number-number*2
out = letternumb - number1

#rev = letter[::-1]
print(letter[out:letternumb])
#print(rev[letternumb:out])
