# practice loop 2 문제8

number1, number2 = map(int,input("입력하시오 :").split())

primecount = 0

numlist=[]

if number1 > 1:
    for x in range(number1,number2+1):
        numlist.append(x)
    for y in numlist:
        count = 0
        for z in range(1,y+1):
            if y%z ==0:
                count +=1
        if count == 2:
            primecount +=1
print(primecount)



