def outer_function(x):
    def inner_function(y):
       return x + y
    return inner_function 
clousure = outer_function(433)
b = clousure(19)
print(b)