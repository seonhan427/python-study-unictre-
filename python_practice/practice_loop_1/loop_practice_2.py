count = 0
sum = 0
number = 0

while number < 100:
    number = int(input("정수를 입력하시오:"))
    
    if number < 100:
        sum = sum + number
        count += 1
avg = sum / count

print("합계:", sum)
print("평균",round(avg,1))

#마지막입력된 수를 포함 해야함!