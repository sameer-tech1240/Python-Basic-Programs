class A:
    def __init__(self, name, name1, year):
        self.__name = name
        self.__name1 = name1
        self.__year = year
        self.__is_sarfaraz = False
    def start(self):
        if not self.__is_sarfaraz:
            print(f"I am sarfaraz {self.__name} {self.__name1}...")
            self.__is_sarfaraz = True
        else:
            print(f"khan{self.__name} {self.__name1} dilshad.")
    def stop(self):
        if self.__is_sarfaraz:
            print(f"........ {self.__name} {self.__name1}...")
            self.__is_sarfaraz = False
        else:
            print(f"The {self.__name} {self.__name1} yasir.")
    def get_name(self):
        return self.__name
    def get_name1(self):
        return self.__name1
    def get_year(self):
        return self.__year
obj_A = A("siddiqui", "....", 999)
print(f"A: {obj_A.get_name()} {obj_A.get_name1()} ({obj_A.get_year()})")
print("Name:", obj_A.get_name())
print("Name1:", obj_A.get_name1())
print("Year:", obj_A.get_year())
