#2021.05.10

class Counter: # 클래스 생성시 첫글자는 대문자!
    def __init__(self): 
        self.count = 0
    
    def reset(self): # initialize count field to 0
        self.count = 0

    def increment(self): # increase count field on a step
        self.count += 1

    def getcount(self): # return a count field
        return self.count

    def setCountDefault(self, initValue):
        self.count = initValue


# create an instance from counter

sample = Counter()

print(sample.getcount())

# visit three participants to gym

sample.increment()
sample.increment()
sample.increment()

print(sample.getcount())

for i in range(100):
    sample.increment()

print('05/09-', sample.getcount())

print(sample.getcount())

sample.setCountDefault(10000)

print()