# 커피문제 
# 가사 검색


# 응용하면 사용자에게 가사단어와 검색 키워드를 입력받는 것도 가능합니다 append 를 이용하면 될꺼같습니다
# 편의상 리스트를 미리 만들어 놓았습니다
# word = ["frodo", "front", "frost", "frozen","frame","kakao"]

# queries = ["fro??","????o","fr???","fro???","pro?"]                 # ,"????o","?????n" 이상없는지 알기위해 추가했던것입니다

word = []
queries = []
#입력단

while True :
    word.append(input("가사 단어를 입력하시오\n다음으로 넘어가려면 0 입력: "))
    if '0' in word:
        word.pop() # 마지막 값을 지우기 위해 사용
        break

while True :
    queries.append(input("찾고싶은 키워드를 입력하시오\n결과를 확인하려면 0 입력: "))
    if '0' in queries:
        queries.pop() # 마지막 값을 지우기 위해 사용
        break


endwith = []  # ~으로 끝나는 단어 리스트
endwithnum = [] # ~으로 끝나는 단어 글자수 리스트
startwith = [] #~으로 시작하는 단어 리스트
startwithnum =[] #~으로 시작하는 단어 글자수 리스트
letter = 'abcdefghijklmnopqrstuvwxyz' # 물음표를 제외한 단어만을 정리하기 위한 조건문을 위한 변수
bigletter ='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #위와 동일
# 결과 출력을 위한 코드
for x in queries:
    if x.startswith("?"): 
        let =''
        for y in x:
            if y in letter or y in bigletter: #물음표를 제거하고 나머지 단어만 정리
                let += y
        endwith.append(let) # ~으로 끝나는 단어 단어만 정리, ?를 제거함
        endwithnum.append(len(x)) # ~으로 끝나는 단어의 글자수 정리
    else:
        let2 = ''
        for y in x:
            if y != '?': 
                let2 += y
        startwith.append(let2) # ~으로 시작하는 단어만 정리, ?를 제거함
        startwithnum.append(len(x)) #~으로 시작하는 단어의 글자수 정리 

# print(endwith)           #확인하기 위해 만든 프린트 문입니다.
# print(endwithnum)
# print(startwith)
# print(startwithnum)

result = [] # 결과 출력을 위한 리스트선언
idx = 0 # 리스트의 순서를 바꾸기 위해 0으로 변수를 만들었습니다
idx2 = 0 # 리스트의 순서를 바꾸기 위해 0으로 변수를 만들었습니다
for x in queries:
    if x.startswith("?"):
        count =0   # 매 카운트 마다 초기화를 위해 지정
        for y in word:
            if y.endswith(endwith[idx]) and len(y) == endwithnum[idx]: # ?를 제외한 ~으로 끝나고 단어의 수가 똑같으면 카운트
                count += 1
        result.append(count)
        idx += 1 # 리스트의 순서를 다음으로 보내기위해 숫자를 증가시킵니다
    else:
        count = 0 # 매 카운트 마다 초기화를 위해 지정
        for y in word:
            if y.startswith(startwith[idx2]) and len(y) == startwithnum[idx2]: # ?를 제외한 ~으로 시작하고 
                count += 1     
        result.append(count)
        idx2 += 1   # 리스트의 순서를 다음으로 보내기위해 숫자를 증가시킵니다

print(result)            







#아이디어 짜던것들입니다
# wordlen = []
# for x in queries:
#     count = 0
#     for y in x:
#         if y == "?":
#             count += 1
#     wordlen.append(count)

# print(wordlen)
