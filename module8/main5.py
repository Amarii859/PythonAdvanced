class MyClass:
    def __inif__(self):
        self.__private_variable = "This is a privat variable"

    def __privat_method(self):
        print("This is a privat method")


my_class = MyClass()




print(my_class.__private_variable)