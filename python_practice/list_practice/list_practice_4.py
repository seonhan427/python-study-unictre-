#list practice 문제4

class_score = [85.6,79.5,83.1,80.0,78.2,75.0]

#input 을 옆으로 나란히 받기 위해 map 함수 사용
classnum1, classnum2 = map(int,input("반을 입력하시오: ").split())
sum = class_score[classnum1-1]+class_score[classnum2-1]
print(round(sum,1)) # 소수점 1자리까지만 출력