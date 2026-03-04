from module11.challange import DS_Prishtina


class DigitalSchool :
    def __init__(self, name , city , state , courses):
        self.__name = name
        self.__city = city
        self.__state = state
        self.__courses = courses


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self , value):
        self.__name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def state(self):
        return self.__state

    @city.setter
    def state(self, value):
        self.__state = value

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        self.__courses = value

    def show_school_info(self):
        return{
            "Name": self.__name,
            "City": self.__city,
            "State": self.__state,
            "Courses": self.__courses
        }

    def organize_heckathon(self):
        print("Heckathon")

    class DS_Prishtina(DigitalSchool):
        def __init__(self, name , city , state , courses , student_number):
            super().__init__(name , city , state , courses)
            self.__student_number = student_number

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, value):
        self.__student_number = value


     def SCF(self):
         print("hello")

    def oragnize_hackathon(self):
        print("welcome")



ds = DS_Prishtina(
    "Shkolla Digjitale"
    "Pejton",
    "Kosova",
    "PHP , HTML ",
    250

)

ds.SCF()
ds.organize_hackathon()

print(f"numri i nxenseve ne shkollen digjitale eshte {ds.student_number}")
print(ds.show_school_info())


