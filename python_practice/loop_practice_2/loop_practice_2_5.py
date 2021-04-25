# practice loop 2 문제5

number = []

while True:
    number.append(int(input("입력:")))
    if -1 in number:
        number.pop()
        break
if len(number) < 3:
    print(number)
else:
    print(number[-3],number[-2],number[-1])

