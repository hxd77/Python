import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态,就不断模拟随机游走
while True:
    #创建一个RanddomWalk实例
    rw=RandomWalk()
    rw.fill_walk()

    #将所有点都绘制出来
    plt.style.use('classic')
    fig,ax=plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    ax.set_aspect('equal')  #指定两条轴上刻度的间距必须相等
    plt.show()

    keep_running=input("Make another walk? (y/n)")
    if keep_running == 'n':
        break