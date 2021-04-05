# def 함수이름 (매개변수1, 매개변수2):          <- 헤드, 시그니처  
#   문장1                                     <- 바디
#   문장2

#parameter = input, 입력

#함수선언은 최상단으로 보내야함 / 함수는 상단에 미리 정의되어야만 밑에서 사용가능

#def main()
#main()      <-- 이런 형태는 가능

#ex)
def square(n):
    return(n*n)
print(square(10))


#ex2)

def get_max(x,y):
    if x > y:
        return x
    else:
        return y


    if x > y:
        result = x
    else:
        result = y
    
    return result




