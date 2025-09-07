from random import choice

#choice表示随机从一个序列中选出元素
class RandomWalk:
    """生成一个随机游走的属性"""
    #有三个属性，一是跟踪随机游走次数的变量，二是跟踪x坐标值，三是跟踪y坐标值
    def __init__(self,num_points=5000):#num_points表示游走包含的默认点数
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有随机游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走包含的所有点"""

        #不断游走，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            #决定前进方向以及沿这个方向前进的距离
            x_direction=choice([-1,1]) #向左还是右
            x_distance=choice([0,1,2,3,4,5,6,7,8])  #前进的距离
            x_step=x_direction*x_distance

            y_direction=choice([-1,1])  #向上还是下
            y_distance=choice([0,1,2,3,4,5,6,7,8])
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue

            #计算下一个点的x坐标值和y坐标值
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)


