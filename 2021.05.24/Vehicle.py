class Vehicle:
    def __init__(self, name):
        self.name = name

class Truck(Vehicle):
    def drive(self):
        return '트럭을 운전합니다.'

class car(Vehicle):
    def drive(self):
        return '승용차를 운전합니다.'


Vehiclelist = [Truck('truck1'),Truck('truck2'),car('car1')]

for x in Vehiclelist:
    print(x.name,':',x.drive())
