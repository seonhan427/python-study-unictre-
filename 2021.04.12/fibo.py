#import 사용 

import fibo

fibo.fib(1000)


# 빌트인 함수화 시키는것 
from fibo import *  # * 은 모두를 의미 특정 함수나 클래스만 지정도 가능

fib(500)