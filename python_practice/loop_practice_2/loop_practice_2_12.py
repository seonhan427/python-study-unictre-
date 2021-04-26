# practice loop 2 문제12

key = input("키값을 입력하시오:")
string = input("복호화할 문장을 입력하시오:")
string = list(string)
key = list(key)
bignumber ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
output = ''
for letter in string:
    for x in key:
        if x == letter:
            number = ord(letter)+(key.index(x))
            output += chr(number)
print(output)
        
        # if letter in bignumber:
            
        # else:
        #     continue

        # 미완성했습니다....
    

