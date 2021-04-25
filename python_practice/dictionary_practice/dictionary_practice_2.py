#딕셔너리 실습 문제2

icecream = {'Tankboy' : 1200, 'Ppangppare' : 1800, 'Worldcorn' : 1500, 'Melona' : 1000}

minvalue = min(icecream, key=icecream.get)
print(minvalue)