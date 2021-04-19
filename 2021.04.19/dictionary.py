myDiction = {}

myDiction['one'] = '하나'
myDiction['two'] = '둘'
myDiction['three'] = '셋'

letter = input("단어를 입력하시오: ")

if letter in myDiction:
    print(myDiction[letter])
else:
    print("없음")

# .get 은 value출력과 세트에 없을시 출력해줄수있는 기능이 있음

print(myDiction.get(letter,"없음")) # .get 을 사용한 응용