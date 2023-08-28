class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open")


my_dog = Restaurant('willie', 'Russian')
my_dog1 = Restaurant('willie1', 'Russian')

my_dog.describe_restaurant()
my_dog.open_restaurant()
my_dog1.describe_restaurant()
