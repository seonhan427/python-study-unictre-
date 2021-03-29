s = 0
for i in range(0,101,3):
    s = s + i
print("1부터 100사이의 모든 3의 배수의 합은",s,"입니다.")

i = 0
z = 0
while i <101:
    z = z + i
    i = i + 3
print("1부터 100사이의 모든 3의 배수의 합은",z,"입니다.")


z = 0
for i in range(1,101):
    if i%3 == 0:
        z = z + i
print("1부터 100사이의 모든 3의 배수의 합은",z,"입니다.")
     