#餐馆
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("Eestaurant name is "+self.restaurant_name.title()+".")
        print("Eestaurant cuisine type is "+self.cuisine_type.title()+".")

    def open_restaurant(self):
        print("The restaurant is open.")
my_restaurant=Restaurant("kfc",'fast food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()