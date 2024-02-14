class MyClassOne:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

# Create an instance of MyClassOne
obj_one = MyClassOne(attribute1="Hello", attribute2="World")

# Access instance variables using dot notation
print(obj_one.attribute1)
print(obj_one.attribute2)

# Access instance variables using getattr
print(getattr(obj_one, 'attribute1'))
print(getattr(obj_one, 'attribute2'))

# Update instance variable dynamically
setattr(obj_one, 'attribute1', 'NewValue1')
print(obj_one.attribute1)

# Delete instance variable dynamically
delattr(obj_one, 'attribute2')

class MyClassTwo:
    def access_from_another_class(self, obj):
        # Access instance variables using dot notation
        print(obj.attribute1)
        # Access instance variables using getattr
        print(getattr(obj, 'attribute1'))

# Create an instance of MyClassTwo
obj_two = MyClassTwo()

# Access instance variables from MyClassOne in MyClassTwo
obj_two.access_from_another_class(obj_one)
                                                         
                                                           