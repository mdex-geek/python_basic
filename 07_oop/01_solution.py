class Car:
    total_car=0
    def __init__(self,brand ,model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand+"!"
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_discription():
        # we have link it 
        return 'car are  means of transport '
    @property
    def model (self):
        return self.__model

class ElectricCar(Car):
    # inheritance 
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)     
        self.batterysize=batterySize
    
    def fuel_type(self):
        return 'electric charge'


# we have to link them car and my_car use keyword "self"
# car = Car("tata", "safari")

# print(car.get_brand(),car.model)
# print(car.fuel_type())
# print(car.total_car)
# print(car.model)


# my_car = ElectricCar("tesla","Model S","90kwh")

# print(isinstance(my_car,Car))
# print(isinstance(my_car,ElectricCar))

class Battery:
    def Battery_info(self):
        return 'this is battery'

class Engine:
    def engine_info(self):
        return 'this is engine'

class ElectricCarTwo(Battery,Engine,Car):
    pass


my_tesla_car= ElectricCarTwo('tesla','modal M')
print(my_tesla_car.Battery_info(),my_tesla_car.engine_info())
