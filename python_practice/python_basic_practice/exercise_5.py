# python basic practice 문제 5

letter, number = input("입력하시오 : ").split(' ')

number1 = int(number)
number2 = number1-1

newletter = letter.replace(letter[number2], '')

print(newletter)