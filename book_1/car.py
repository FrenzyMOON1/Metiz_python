class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer += mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        print("This car is full")


class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a battery of " + str(self.battery_size) + "%.")

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank")


my_car = Electric_car('Tesla', 'Model S', '2023')
print(my_car.get_descriptive_name())
my_car.describe_battery()
my_car.fill_gas_tank()

my_new_car = Car('Ford', 'Mustang', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()
