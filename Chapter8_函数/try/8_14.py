#汽车
def make_car(car_brand,car_with,**car_info):
    car_profile={}
    car_profile['car_brand']=car_brand
    car_profile['car_with']=car_with
    for key,value in car_info.items():
        car_profile[key]=value
    return car_profile
car=make_car('subaru','outbreak',color='blue',tow_package=True)
print(car)