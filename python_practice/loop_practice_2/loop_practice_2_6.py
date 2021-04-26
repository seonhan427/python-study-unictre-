# practice loop 2 문제6
string = list(input("입력 문자열:"))
# print(string)

letter = input("찾고 싶은 문자:")
string.index(letter)

#enumerate 을 사용해서 여러개의 인덱스 값을 찾았습니다
output = [idx for idx, let in enumerate(string) if let == letter]
print(output)