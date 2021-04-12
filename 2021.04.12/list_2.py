scores = []

for x in range(5):
    scores.append(int(input("성적을 입력하시오:")))
x = 0    
add = 0
for y in scores:
    add += y
    if y >=80:
        x += 1
print("성적 평균은",add/5,"입니다")
print("80점 이상 성적을 받은 학생은",x,"명 입니다.")


# 공백처리시 ''로

# index() list형 자료에서 위치를 찾을때 사용

# pop()는 특정한 위치에 있는 항목을 삭제한다
# remove 는 값을 알고있을때 사용
# list 는 비교연산자사용 가능 >,<는 길이를 비교
# min, max

# sort() 숫자 순서 정렬 함수 -> sorted() 는 리턴값을 줌

#복사 방법! ex) 깊은 복사 values = list(scores) 

#리스트 함축

# row행 clo열 순서로 꺼내올것 !