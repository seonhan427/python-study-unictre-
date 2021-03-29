sum = 0
score = 0
count = 0

print("종료하려면 음수를 입력하시오")

while score >=0:
    score = int(input("성적을 입력하시오: "))

    if score >= 0:
        #사용자가 입력한 성적을 누적
        sum = sum + score
        # 평균을 계산할 때 사용할 입력횠수 설정(조정)
        count = count + 1

avg = sum / count
print("평균 : ", avg)



# break 반복문 빠져나가는 


# score = 0
# count = 0
# S = 0

# while score >= 0 :
#     score = float(input("성적을 입력하시오: "))
#     S = 
# print("성적의 평균은","입니다." )