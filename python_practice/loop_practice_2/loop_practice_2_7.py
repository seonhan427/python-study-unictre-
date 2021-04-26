# practice loop 2 문제7

scorelist = []

ten=0
nine=0
eight=0
seven=0
six=0
five=0
four=0
three=0
two=0
one=0
zero=0

while True:
    score = int(input("점수를 입력하시오: "))
    if score == 0:
        break
    scorelist.append(score)
for x in scorelist:
    if x == 100:
        ten += 1
    elif x < 100 and x >= 90:
        nine += 1   
    elif x < 90 and x >= 80:
        eight += 1
    elif x < 80 and x >= 70:
        seven += 1
    elif x < 70 and x >= 60:
        six += 1
    elif x < 60 and x >= 50:
        five += 1
    elif x < 50 and x >= 40:
        four += 1
    elif x < 40 and x >= 30:
        three += 1
    elif x < 30 and x >= 20:
        two += 1
    elif x < 20 and x >= 10:
        one += 1
    elif x < 10 and x >= 1:
        zero += 1
        
if ten > 0:
    print("100 :",ten,"person")
if nine > 0:
    print("90 :",nine,"person")
if eight > 0:
    print("80 :",eight,"person")
if seven > 0:
    print("70 :",seven,"person")
if six > 0:
    print("60 :",six,"person")
if five > 0:
    print("50 :",five,"person")
if four > 0:
    print("40 :",four,"person")
if three > 0:
    print("30 :",three,"person")
if two > 0:
    print("20 :",two,"person")
if one > 0:
    print("10 :",one,"person")
if zero > 0:
    print("1 :",zero,"person")















    
