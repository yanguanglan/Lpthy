# -- coding:utf-8 --

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# dog
class Dog(Animal):
    def __init__(self, name):
        self.name = name

# cat
class Cat(Animal):
    def __init__(self, name):
        self.name = name

# person
class Person(object):
    def __init__(self, name):
        self.name = name
    
        self.pet = None
    
# employee
class Employee(Person):
    def __init__(self, name, salary):
    
        super(Employee, self).__init__(name)
    
        self.salary = salary

# fish
class Fish(object):
    pass

#salmon
class Salmon(Fish):
    pass

# Halibut
class Halibut(Fish):
    pass
    
# rover is-a Dog    
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
   