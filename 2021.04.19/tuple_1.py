
import math

pi = math.pi

def calC(r):
    area = pi*r**2
    length = 2*pi*r
    return(area , length)
    


r = float(input("원의 반지름을 입력하시오: "))
answer = calC(r)
print("원의 넓이는",answer[0],"이고 원의 둘레는",answer[1],"이다.")
    
# (a,c) = claC(r)
# print()