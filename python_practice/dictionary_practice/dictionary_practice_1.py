#딕셔너리 실습 문제1

icecreamdict = {}

icecreamdict['melona'] = [1000,10]
icecreamdict['pollapo'] = [1200,7]
icecreamdict['ppangppare'] = [1800,6]
icecreamdict['tankboy'] = [1200,5]
icecreamdict['heathunting'] = [1200,4]
icecreamdict['worldcorn'] = [1500,3]

for key in icecreamdict.keys():
    print(key,icecreamdict.get(key),sep="       ")


