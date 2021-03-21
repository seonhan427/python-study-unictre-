#python basic practice 문제 3
#완벽하게 해결하지 못함

letter, number = input("입력하시오 : ").split(' ')
#number = int(input("숫자를 입력하시오 : "))

number1 = int(number)

letternumb = len(letter)
out = letternumb - number1


string = letter[out:letternumb]
reversedstring = "".join(reversed(string))

print(reversedstring)

