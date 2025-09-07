import matplotlib.pyplot as plt
from random_walk import RandomWalk

#制作一个随机游走
rw=RandomWalk(5_000)
rw.fill_walk()

#将所有点都绘制出来
plt.style.use('classic')
fig,ax=plt.subplots()
point_numbers=range(rw.num_points)
ax.plot(rw.x_values,rw.y_values,linewidth=1)
ax.set_aspect('equal')  #指定两条轴上刻度的间距必须相等

#强调最开始和最后一个点
ax.scatter(0,0,c="green",edgecolors='none',s=15) #s表示大小
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=15)

#移除坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()