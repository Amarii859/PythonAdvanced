class Animal:

    def __init__(self,name):

        self.name = name

    def sound(self):
        print("some genetic")

    def description(self):
        print("gentetic")

class Dog(Animal):

    def __init__(self,name,breed):

        super().__init__(name)

        self.breed = breed

    def sound(self):
        print("woof ,woof")

    def description(self):
        super().description()

        print(f"Breed : {self.breed}")


class Cat(Animal):

    def __init__(self, name, color):
        super().__init__(name)

        self.color = color

    def sound(self):
        print("woof ,woof")

    def description(self):
        super().description()

        print(f"color : {self.color}")


animal = Animal("generic animal")

animal.sound()

animal.description()



dog = Dog("Rex" , "Golden Retriver")

dog.sound()

dog .description()

cat = Cat("Rex" , "Golden Retriver")

cat.sound()

cat .description()










