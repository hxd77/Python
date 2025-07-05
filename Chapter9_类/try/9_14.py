#骰子
from random import randint
x=randint(1,6)
print(x)
class Die:
    def __init__(self,sides=6):
        '''初始化属性骰子的面数'''
        self.sides=sides

    def roll_die(self):
        '''显示位于1和骰子面数之间的随机数'''
        print(randint(1,self.sides))

sides_num=[6,10,20]
for sides in sides_num:
    sides_die=Die(sides)
    print(str(sides)+"面骰子掷10次:")
    for i in range(10):
        sides_die.roll_die()