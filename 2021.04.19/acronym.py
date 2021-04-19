acr = input("문자열을 입력하시오: ")

acrlist = acr.split()

acr2 = ''
for letter in acrlist: # .upper .lower
    acr2 += letter[0]
print(acr2) 