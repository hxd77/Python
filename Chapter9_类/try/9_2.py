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
restaurant1=Restaurant("kfc",'fast food')
restaurant2=Restaurant("mcdonalds",'fast food')
restaurant3=Restaurant("Chinese restaurant",'Chinese food')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
