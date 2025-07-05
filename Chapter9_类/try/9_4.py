#就餐人数
#餐馆
from threading import main_thread


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_serverd=0
    def describe_restaurant(self):
        print("Eestaurant name is "+self.restaurant_name.title()+".")
        print("Eestaurant cuisine type is "+self.cuisine_type.title()+".")

    def open_restaurant(self):
        print("The restaurant is open.")

    def read_number_serverd(self):
        '''打印一条指出餐馆就餐人数的信息'''
        print("The restaurant has served "+str(self.number_serverd)+" people.")

    def set_number_serverd(self,number):
        self.number_serverd=number

    def increment_number_serverd(self,add_number):
        self.number_serverd+=add_number
        
my_restaurant=Restaurant("kfc",'fast food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.read_number_serverd()
my_restaurant.number_serverd=10
my_restaurant.read_number_serverd()

my_restaurant.set_number_serverd(40)
my_restaurant.read_number_serverd()

my_restaurant.increment_number_serverd(50)
my_restaurant.read_number_serverd()