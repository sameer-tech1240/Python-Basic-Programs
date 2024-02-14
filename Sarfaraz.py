class Private:
     def __init__(self):
        self.__private = "I am private"
     def access_private_method(self):
        return self.__private
obj=Private()
result = obj.access_private_method()
print("Accessing private attribute using a method:", result)

result_mangling = obj._Private__private
print("Accessing private attribute using name mangling:", result_mangling)
