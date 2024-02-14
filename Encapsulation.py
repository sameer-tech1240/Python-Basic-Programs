class Car:
    def __init__(self, make, model, year):
        self.__make = make      
        self.__model = model     
        self.__year = year      
        self.__is_running = False 
    def start(self):
        if not self.__is_running:
            print(f"Starting the {self.__make} {self.__model}...")
            self.__is_running = True
        else:
            print(f"The {self.__make} {self.__model} is already running.")
    def stop(self):
        if self.__is_running:
            print(f"Stopping the {self.__make} {self.__model}...")
            self.__is_running = False
        else:
            print(f"The {self.__make} {self.__model} is already stopped.")
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year
my_car = Car("Toyota", "Camry", 2022)
print(f"Car: {my_car.get_make()} {my_car.get_model()} ({my_car.get_year()})")
my_car.start()
my_car.stop()
my_car.start()
my_car.start()
my_car.stop()