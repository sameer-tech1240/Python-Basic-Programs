#Closure in Python is an inner function object, a function that behaves like an object,
def great():
    name = "Sameer"
    # print("hey"+name)
    return lambda : "Hey" + name
message = great()
print(message())