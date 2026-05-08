class car:
    def __init__(self,brand):
        self.brand = brand

car1=car("Audi")
car2=car("Toyota")

print(car1.brand)  #Audi
print(car2.brand)  #Toyota

"""
def → defines a function
__init__ → special function (runs automatically when object is created)
self → refers to the current object
brand → input you give (like "Audi")

“Whenever a car is created, store its brand”
Take the input (brand) and store it inside this object

class Car → blueprint created
"""


#eg 2:
class Car:
    wheels =4                  #class variable
    def __init__(self,brand):
        self.brand = brand

car1=Car("Audi")
car2=Car("Toyota")

car1.wheels =6                #new  instance variable

print(car1.wheels) # 6
print(car2.wheels) #4
print(Car.wheels) #4



"""
Create a class called Car
Add an __init__ method with a brand parameter, and store it as a property
Add a method called show that prints the brand
Create an object c1 of the Car class with brand "Ford"
Call the show method on c1

"""
class Car:
    def __init__(self,brand):
        self.brand = brand

    def show(self):
        print(self.brand)
c3=Car("Ford")
c3.show()

"""
Instance variables override class variables for that specific object.

Class = shared rule → “All cars have 4 wheels”
c1 says → “Mine has 6 wheels now”
c2 still follows original rule

"""

"""
car1 = Car("Audi")
    → new object created
    → brand = "Audi

car2 = Car("Toyota")
    → new object created
    → brand = "Toyota"

print(car1.brand) → Audi
print(car2.brand) → Toyota

One-Line Summary:-

A class defines structure,
__init__ initializes data,
self stores data inside each object.

"""







