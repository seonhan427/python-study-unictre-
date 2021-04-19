
flie = open('C:/A/word.txt','r')

# wordset = set()
word_dict = dict()

count = 0
for line in flie:
    words = line.split()
    # for word in words:
    # #     wordset.add(word)
    # for word in words:
    #     word_dict[word] = '1'  # 카운트??????????


    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1


# print(wordset)
print(word_dict)
print(flie)
        
