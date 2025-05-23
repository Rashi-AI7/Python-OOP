class Animal:
    def make_sound(self ):
        print("Make some sound!")

class Dog(Animal):
    def bark(self):
        print(f"Woof!")
    
class Cat(Animal):
    def meow(self):
        print(f"Meow!")

a = Animal()
a.make_sound()

d = Dog()
d.bark()

c = Cat()
c.meow()
