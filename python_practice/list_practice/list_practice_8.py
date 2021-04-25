#list practice 문제8

numbers = []

for x in range(10):
    numbers.append(int(input("숫자를 입력하시오: ")))

numbers.sort(reverse=True)
print(numbers)
