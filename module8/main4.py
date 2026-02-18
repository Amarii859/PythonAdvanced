class Student:
    school_name = "digital School"

    def __init__(self, name , age , course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Dreni" , 16 , "Python")

print(student1.course)