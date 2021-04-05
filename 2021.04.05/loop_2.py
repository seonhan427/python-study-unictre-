sentence = input("문자열을 입력하시오:")

letter= "abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
number ="0123456789"
space = " "

x = 0
y = 0
z = 0
for string in sentence:
    if string in letter:
        x += 1
    if string in space:
        y += 1
    if string in number:
        z += 1    
print("알파벳 문자의 개수=",x)
print("스페이스의 개수=",y)
print("숫자문자의 개수=",z)
