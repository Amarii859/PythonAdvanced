import streamlit as st
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            st.error("Weight must be positive")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            st.error("Height must be positive")

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

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
        return self.weight / ((self.height / 100) ** 2)

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


# Streamlit UI
st.title("BMI Calculator App")

name = st.text_input("Enter Name")
age = st.number_input("Enter Age", min_value=0, step=1)
weight = st.number_input("Enter Weight (kg)", min_value=0.0)
height = st.number_input("Enter Height (cm)", min_value=0.0)

if st.button("Calculate BMI"):
    if name and weight > 0 and height > 0:
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        bmi = person.calculate_bmi()
        category = person.get_bmi_category()

        st.subheader("Result")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Weight: {weight} kg")
        st.write(f"Height: {height} cm")
        st.write(f"BMI: {round(bmi, 2)}")
        st.write(f"Category: {category}")
    else:
        st.warning("Please fill all fields correctly.")