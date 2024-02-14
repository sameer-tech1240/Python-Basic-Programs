                                #Custom Iterator
class MyCustom:
    def __init__(self, start , end):
        self.start = start
        self.end = end

    def __iter__(self):
            return self
        
    def __next__(self):
            if self.start >= self.end:
                raise StopIteration
            
            else:
                result = self.start
                self.start +=1
                return result
my_custom= MyCustom(1,4)
for number in my_custom:
    print(number)    
print("----------------------------------------------------")
                      #Iterate List By Loop

list = [2,3,1,4,5,6]
number = iter(list)
for i in number:
    print(i) 
print("----------------------------------------------------")

                              #Iterate list using iter()
list = [1,2,3,4,5]
iterator = iter(list)
print((next(iterator)))
print((next(iterator)))
print((next(iterator)))
print((next(iterator)))
print((next(iterator)))
                           #Task Completed By Sameer
                                       
