
class Animal:
    def speak(self):
        print("tu padh nahi sakta")

class Yasir:
    def give_birth(self):
        print("main ja raha jdbc padhne")

class Afsar:
    def take_lecture(self):
        print("aaj hum padhege python")

class Sameer(Animal):
    def bark(self):
        print("padh lo tu iska matlab yeh nahi ke dosro ko padhne na do")

class Bat(Animal, Yasir, Afsar):
    def fly(self):
        print("tu khali udte reh")

bat = Bat()  
bat.speak()      
bat.give_birth() 
bat.take_lecture()   
bat.fly()        
