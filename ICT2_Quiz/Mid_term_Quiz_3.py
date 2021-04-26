import random

comnumber = []

rannum = random.randint(0,9)

for x in range(3):
    while rannum in comnumber:
        rannum = random.randint(0,9)
    comnumber.append(rannum)
#print(comnumber)


while True:
    usernumber = map(int,input("3개의 숫자를 입력하시오:"))
    usernumlist = list(usernumber)
#    print(usernumlist)
    if usernumlist == comnumber:
        print("3 strike 0ball 0out 사용자의 승리입니다!!")
        break
    strike = 0
    ball = 0
    out = 0
    for x in range(3):
        if usernumlist[x] == comnumber[x]:
            strike += 1
        elif usernumlist[x] in comnumber:
            ball += 1
        elif usernumlist[x] not in comnumber:
            out +=1
    print(strike,"strike",ball,"ball",out,"out")



#        여기는 실패한것들입니다~
#     if int(usernumber) == comnumber:
#         print("3 strike 0ball 0out 사용자의 승리입니다!!")
#         break
#     usernumber1 = list(usernumber)
#     for y in usernumber:
#         for x in range(3):
#             if str(comnumber)[x] == y:
#                 strike += 1
#             elif str(comnumber)[x] != y and y in str(comnumber):
#                 ball += 1
#         if y not in str(comnumber):
#             out +=1
#     print(strike,"strike",ball,"ball",out,"out")
#     print(comnumber)
#     continue

        
    