class Prey:

    def flee(self):
        print('This animal flees')

class Predator:
    def hunt(self):
        print('This animal is huntimg')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
#hawk.hunt()
fish.flee()
fish.hunt()