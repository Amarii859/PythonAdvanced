from abc import ABC ,abstractmethod

from numpy.random import choice

from module12.challange1 import BMIApp


class Person(ABC):
    def __init__(self,name, weight , hight , age ,):
        self.name = name
        self.weight = weight
        self.hight = hight
        self.age = age


    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self , value):
        if value > 0:
            self._weight = value
        else:
            print("duhet qe pesha te jete pozitive")

    @property
    def hight(self):
        return self._weight

    @hight.setter
    def hight(self, value):
        if value > 0:
            self._hight = value
        else:
            print("duhet qe gjatesia te jete pozitive")

    @abstractmethod
    def calculator_bmi(self):
        pass


    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculator_bmi()
        category = self.get_bmi_category()

        print("Name:",self.name)
        print("Weight:", self.weight ,"kg")
        print("Hight:", self.hight, "cm")
        print("Age:", self.age)
        print("BMI:" , round(bmi))
        print("Catergory:" , category)

class Adult(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class Child(Person):

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"

class BMIapp :
    def __init__(self):
        self.people = []

    def add_person(self,person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter Name :")
        age = int(input("Enter Age :"))
        weight = float(input("Enter Weight (kg) :"))
        height = float(input("Enter Height (cm) :"))

        if age >= 18 :
            person = Adult(name, age, weight, height)
        else:
            person = Child(name , age , weight , height)

        self.add_person(person)

    def print_result(self):
        print("\n=== BMI RESULT ===")
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            choice = input("\nAdd another person ? (y/n)").lower()

            if choice != "y":
                break

            self.print_result()

if __name__ == "__main__":
    app = BMIApp()
    app.run()









































