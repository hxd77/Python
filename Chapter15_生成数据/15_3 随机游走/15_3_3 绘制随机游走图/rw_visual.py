import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RanddomWalk实例
rw=RandomWalk()
rw.fill_walk()

#将所有点都绘制出来
plt.style.use('classic')
fig,ax=plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15)
#ax.set_aspect('equal')  #指定两条轴上刻度的间距必须相等
plt.show()