from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print('you ride the car')

    def stop(self):
        print('this car is stoping')

class Motorcycle(Vehicle):

    def go(self):
        print('you ride the motorcycle')

    def stop(self):
        print('you stapd the motorcycle')

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()