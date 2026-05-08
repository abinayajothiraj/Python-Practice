# can methods be deleted?
#yes. Methods can be deleted from a class using the del keyword.
#Since methods belong to the class , deleting a method affects all objects created from that class.

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")

# creating an object
p1=Person("Buddy")

#calling  the object before deletion
p1.greet()

#deleting method from the class
del Person.greet

print("\nMethod Deleted\n")

#calling method after deletion
p1.greet()  #op: AttributeError