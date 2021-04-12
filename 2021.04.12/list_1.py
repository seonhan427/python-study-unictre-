scores = []
for i in range(10):
    scores.append(int(input("성적을 입력하시오:"))) #append 사용!
print(scores)
print(scores[5])


scores = [10,11,12,13,14,15,16,17,18,19]
for element in scores:
    print(element)


#list 의 특정값을 바꿀시에는 인덱스 사용!

print(list(range(0,5)))