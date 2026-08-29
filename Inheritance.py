class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Woof!")


dog = Dog()

dog.eat()
dog.bark()