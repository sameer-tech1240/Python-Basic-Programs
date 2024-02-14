class Access:
     def __init__(self):
        self.__private_attribute = "I am private"
     def access_private_method(self):
        return self.__private_attribute
obj=Access()
result = obj.access_private_method()
print("Accessing private attribute using a method:", result)

result_mangling = obj._Access__private_attribute
print("Accessing private attribute using name mangling:", result_mangling)
