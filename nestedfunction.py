def outer_function(x):
    print("Outer Function" , x)
    def inner_function(y):
        print("Inner Function")
        print("Inner Function with variable" , y)
        inner_function(10)
outer_function(12)
