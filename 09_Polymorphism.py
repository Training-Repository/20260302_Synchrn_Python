from random import randint

class Animal:
    def Eat(self):
        print("Eating...")

    def Speak(self):
        print("Speaking...")

# class Cat(Animal):
class Cat:
    def Eat(self):
        print("Nibble...")

    def Speak(self):
        print("Meow...")

# class Dog(Animal):
class Dog:
    def Eat(self):
        print("Gobble...")

    def Speak(self):
        print("Woof...")

# class Cow(Animal):
class Cow:
    def Eat(self):
        print("Munch...")

    def Speak(self):
        print("Moo...")

class Owl:
    def Eat(self):
        print("Peck...")

    def Speak(self):
        print("Hoot...")

#------------------------------------------

def Communicate(an: Animal):
    an.Speak()                          # Duck Typing - If it walks like a Duck, and it Talks like a Duck... It is a Duck


Communicate(Cat())
obj: Animal
choice = randint(1, 3)
match (choice):
    case 1:
        obj = Cat()
    case 2:
        obj = Dog()
    case 3:
        obj = Cow()

Communicate(obj)

Communicate(Owl())

# c = Cat()
# c.Eat()
# c.Speak()