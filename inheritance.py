# Inheritance

class Car:
    @staticmethod
    def start():
        print("The car is started.....")

    @staticmethod
    def stop():
        print("The car is  stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        self.brand = "Fortuner"

car1 = Fortuner("Disele")
car1.start()
print(car1.type)
car2 = ToyotaCar("Fortuner")
print(car1.brand)
print(car2.brand)




