s = input("문자열을 입력하시오: ")

b = "aeiouAEIOU"

x = 0
y = 0

for letter in s:
    if letter in b:
        x += 1
    else:
        y = y + 1    
print("모음의 개수", x)
print("자음의 개수", y)

# for letter in s:
#     if letter in b:
#         x = x + 1
#     print("모음의 개수", x)
#     if letter not in b:
#         y = y + 1
#     print("자음의 개수", y)

# x = x+1  => x += 1

