from cars import Car, ElectricCar
import cars # this way will import every class in the module and they will need to be accessed using car.SomeClass

my_old_car = Car("Ford", "Fiesta", 2015)

print(my_old_car.get_descriptive_name())