salefile = open("sales.txt","r")

count = 0
sum = 0

saleline = salefile.readlines()
for number in saleline:
    sum += int(number) 
    count += 1


salefile.close() #닫는 것은 항상 중요!

print(sum,count)
avg = sum/count


summaryfile = open("summary.txt","w", encoding="UTF=8")

summaryfile.write("총매출 = "+str(sum)+"\n")
summaryfile.write("평균 일매출 = "+str(avg))

summaryfile.close()