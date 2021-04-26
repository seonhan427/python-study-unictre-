# practice loop 2 문제4


number = []
bignumber = []
for x in range(10):
    num = int(input("숫자를 입력하시오:"))
    if num >= 100:
        bignumber.append(num)
    elif num < 100:
        number.append(num)
print("100이상의 수중에 가장 작은 수: ",min(bignumber))
print("100미만의 수중에 가장 큰 수: ",max(number))
