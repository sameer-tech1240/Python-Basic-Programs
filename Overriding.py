class Override:
    def function(self):
        print("super function")
class Sub(Override):
    def function(self):
        print("sub class")
        super().function()
class Child(Sub):
    def function(self):
        print("child class")
        super().function()
obj = Child()
obj.function()
