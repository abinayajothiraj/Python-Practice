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

"""

"""
class Car → blueprint created

car1 = Car("Audi")
    → new object created
    → brand = "Audi"

car2 = Car("Toyota")
    → new object created
    → brand = "Toyota"

print(car1.brand) → Audi
print(car2.brand) → Toyota



🔹 One-Line Summary

👉 A class defines structure,
👉 __init__ initializes data,
👉 self stores data inside each object.

"""