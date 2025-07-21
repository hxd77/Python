import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活动状态,就不断模拟随机游走
while True:
    #创建一个RanddomWalk实例
    rw=RandomWalk(50_000)
    rw.fill_walk()

    #将所有点都绘制出来
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9))#调整输出尺寸
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)#edgecolor=none表示删除每个点的轮廓
    ax.set_aspect('equal')  #指定两条轴上刻度的间距必须相等

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    #将绘制起点和终点的代码放在plt.show()代码前面，确保在其他店的上面绘制起点和重点
    plt.show()

    #隐藏坐标轴
    #ax.get_xaxis().set_visible(False)
    #ax.get_yaxis().set_visible(False)


    keep_running=input("Make another walk? (y/n)")
    if keep_running == 'n':
        break