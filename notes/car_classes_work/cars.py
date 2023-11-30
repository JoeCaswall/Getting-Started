class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # This is how you assign default values to class attributes
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name.title()
    
    def get_mileage(self):
        return f"This car has {self.odometer_reading} miles on it."
    
    def set_mileage(self, miles):
        self.odometer_reading = miles

    def add_miles(self, miles):
        self.odometer_reading += miles
    
    def fill_tank(self):
        return "Gas tank full!"
    
my_new_car = Car("audi", "a4", 2024)

print(my_new_car.get_descriptive_name())
print(my_new_car.get_mileage())
my_new_car.add_miles(134)
print(my_new_car.get_mileage())

### Inheritance ###
# When you're writing a new class based on an existing class, you'll often want to call the __init()__ method from the parent class

# It can be helpful to split classes down further and use *instances as attributes* for parent classes.
# For example, if we extended the ElectricCar class we might notice that the class is getting lengthy
# with lots of atributes and methods relating solely to the battery, so we could move these from 
# the class into their own seperate class called Battery.

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."
    
    def get_range(self):
        range = self.battery_size * 3.75
        return f"This car can go roughly {range} miles on full charge"
    
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            return "Battery Upgraded to 65-kWh!"
        else:
            return f"Your car already has a {self.battery_size}-kWh battery installed"


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_tank(self):
        return "This car doesn't take petrol." # You can also override non-relevant methods from the parent class

my_leaf = ElectricCar("nissan", "leaf", 2024)

print(my_leaf.get_descriptive_name()) # The child class inherits any methods from the parent class automatically...
print(my_leaf.set_mileage(120)) 
print(my_leaf.get_mileage())
print(my_new_car.fill_tank())
print(my_leaf.fill_tank()) # ...unless you've overwritten them!

print(my_leaf.battery.describe_battery())
print(my_leaf.battery.get_range())
print(my_leaf.battery.upgrade_battery())
print(my_leaf.battery.upgrade_battery())