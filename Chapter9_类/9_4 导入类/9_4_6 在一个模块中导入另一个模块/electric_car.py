'''一组可用于表示电动汽车的类'''
from car import Car

class Battery:
    '''一次模拟电动汽车电池的简单尝试'''
    def __init__(self,battery_size=75):
        '''初始化电池的属性'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''打印一条描述电池容量的信息'''
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

class ElectircCar(Car):
    '''电动汽车的独特之处'''
    def __init__(self,make,model,year):
        '''初始化父类的属性，再初始化电动汽车特有的属性'''
        super().__init__(make,model,year)
        self.battery=Battery()