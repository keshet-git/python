class Animal:

    alive =True

    def eat(self):
        print('this anial is eating')


    def sleep(self):
        print('this animak is sleepin')


class Rabbit(Animal):
    def run(self):
        print('this rabbit is rsnning')
    
class Fish(Animal):
    def swim(self):
        print('this fish is swimming')
class Howk(Animal):
    def fly(self):
        print('this howk is flying')

rabbit = Rabbit()
fish = Fish()
howk = Howk()

#print(rabbit.alive)
#fish.eat()
#howk.sleep()

rabbit.run()
fish.swim()
howk.fly()