#list practice 문제7

number = []

sum1 = 0
sum2 = 0

for x in range(10):
    number.append(int(input("숫자를 입력하시오: ")))
for y in range(1,10,2):
    sum1 += number[y]
for z in range (0,10,2):
    sum2 += number[z]
avg = sum2 / 5 

print("sum :",sum1)
print("avg :",avg)