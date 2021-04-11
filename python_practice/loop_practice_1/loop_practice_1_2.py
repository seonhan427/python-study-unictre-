# practice loop 1 문제2

number = 0
sum = 0
time = 0

while number < 100:
    number = int(input("수를 입력하시오:"))
    sum += number
    time += 1
print("합계: ", sum)
print("평균: ", round(sum/time,1))