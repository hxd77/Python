def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+". ")

describe_pet('hamster','harry')
describe_pet('dog','willie')

def describe_pet(pet_name,animal_type='dog'):
    #一条名为'Willie'的小狗
    describe_pet('willie')
    describe_pet(pet_name='willie')
    #一只名为Harry的仓鼠
    describe_pet('harry','hamster')
    describe_pet(pet_name='harry',animal_type='hamster')
    describe_pet(animal_type='hamster',pet_name='harry')
