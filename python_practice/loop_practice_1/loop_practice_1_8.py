# practice loop 1 문제8

#동일하게 map을 사용했습니다
x, y = map(int,input("입력하시오:").split())

sum = 0
count = 0
for z in range(x,y+1):
    if z % 3 == 0 or z % 5 ==0:
        sum += z
        count += 1
avg = sum/count
print("sum:",sum,"avg:",round(avg,1))
