class Car():
    '''一次模拟汽车的简单测试'''
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
        self.gas_size=0

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

    def fill_gas_tank(self,gas):
        self.gas_size=gas

