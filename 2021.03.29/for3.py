x = int(input("정수를 입력하시오: "))

z = 1
for y in range(x,0,-1):
    z = z*y 
print(x,"!은 ",float(z),"이다.", sep="")