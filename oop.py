# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age__ = age
#
#     def get_age(self):
#         return self.__age__
#
#     def set_age(self, new_age):
#         if new_age > 0:
#             self.__age__ = new_age
#         else:
#             raise ValueError("Вы ввели неправильное значение")
#
#
# p = Person("Artur", 25)
# p.set_age(25)
# print(p.get_age())
# p.set_age(-5)
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "I am an animal"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# dog = Dog("Buddy")
# cat = Cat("Kitty")
# print(dog.name, dog.speak())
# print(cat.name, cat.speak())

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

car = Car()
bike = Bicycle()
print(car.move())
print(bike.move())
