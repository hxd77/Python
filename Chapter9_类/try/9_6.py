# 冰淇淋小店
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

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours=['apple','pineapple','watermelon','strawberry','blueberry']
        #一个列表用户存储一个由各种口味欸的冰淇淋列表

    def read_icecream_flavours(self):
        for flavour in self.flavours:
            print(flavour)
my_icecreamstand=IceCreamStand('Hagendas','icecream')
my_icecreamstand.read_icecream_flavours()


