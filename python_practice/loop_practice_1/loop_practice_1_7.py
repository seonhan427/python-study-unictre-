# practice loop 1 문제7

#한줄에 받기위해 map함수를 사용하였습니다

x, y = map(int,input("입력하시오:").split())

for z in range(x,y+1):
    print(z,end=' ')