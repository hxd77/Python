from random import choice

#choice表示随机从一个序列中选出元素
class RandomWalk:
    """生成一个随机游走的属性"""
    #有三个属性，一是跟踪随机游走次数的变量，二是跟踪x轴的值，三是跟踪y轴的值
    def __init__(self,num_points=5000):#num_points表示游走包含的默认点数
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有随机游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]