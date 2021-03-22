word = input("문자열을 입력하시오: ")

lennum = len(word)
center = lennum // 2


if lennum % 2 == 0:
    B = center - 1
    print("중앙 글자는 ",word[B],word[center],sep='')
else :
    print("중앙 글자는", word[center])
