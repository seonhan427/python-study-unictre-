class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Temporary(Employee):
    def __init__(self,name,age,ilsu,ildang):
        super().__init__(name,age)
        self.ilsu = ilsu
        self.ildang = ildang
    def show(self):
        print('이름:',self.name,'나이:',self.age,'월급 :',self.ilsu*self.ildang)  

class Regular(Employee):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def show(self):
        print('이름:',self.name,'나이:',self.age,'급여: ',self.salary)

class Salesman(Regular):
    def __init__(self,name,age,salary,sales,commission):
        super().__init__(name,age,salary)
        self.sales = sales
        self.commission = commission
    def show(self):
        print('이름:',self.name,'나이:',self.age,'수령액:',self.salary+self.sales*self.commission)


t = Temporary('홍길동',25,20,15000)
r = Regular('한국인',27,3500000)
s = Salesman('손오공',29,1200000,5000000,0.25)

t.show()
r.show()
s.show()
