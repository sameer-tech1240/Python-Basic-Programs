class Employee:
    def __init__(self , name):
        self.__name=name;
       
    def get_name(self):
        return self.__name;
    def set_name(self, name):
        self.__name = name

emp=Employee("Sameer")
print(f"Student's name: {emp.get_name()}")
emp.set_name("Khan")
print(f"Student's name: {emp.get_name()}")

