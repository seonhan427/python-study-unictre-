#python print practice 문제 4

A, B = input("입력하시오 : ").split()

out1 = A or B
out2 = A and B
print("논리합: ",A,"or",B,"=>",out1)
print("논리곱: ",A,"and",B,"=>",out2)

#질문 false 와 true 입력 순서에 따라 값이 다르게 나옴