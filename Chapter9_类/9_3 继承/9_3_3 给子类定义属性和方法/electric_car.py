class Car():
    '''一次模拟汽车的简单测试'''
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        '''将里程表读数设置为指定的值'''
        '''禁止将里程表回数往回调'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''将里程表读数增加指定的量'''
        self.odometer_reading += miles

class ElectricCar(Car):
    '''电动汽车的独特之处'''

    def __init__(self,make,model,year):
        '''电动汽车的独特之处'''
        '''初始化为父类的属性,再初始化电动汽车特有的属性'''
        super().__init__(make,model,year)
        #super()是一个特殊函数，帮助Python将父类和子类关联起来
        self.battery_size=70

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print("This car has a "+str(self.battery_size)+" battery size.")
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
