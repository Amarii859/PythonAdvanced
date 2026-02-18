class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello i am {self.name} and i am {self.age}")



person1 = Person("Gerti" , 15)
person2 = Person("Dreni" , 16)

person1.greet()
person2.greet()