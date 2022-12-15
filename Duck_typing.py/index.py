class Duck:

    def wolk(self):
        print('This duck is wolking')

    def talk(self):
        print('This duck is qwuacking')

class Chicken:

    def wolk(self):
        print('This ckicken is wolking')

    def talk(self):
        print('This chicken is clocking')

class Person():

    def catch(self, duck):
        duck.wolk()
        duck.talk()
        print('You caught the critter!')

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)