#python basic practice 문제 3

letter = input("문자를 입력하시오: ")
number = int(input("숫자를 입력하시오: "))

letternum = len(letter)
outletter = letter[number-1:letternum]

print(outletter[::-1])
