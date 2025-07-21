import matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
fig,ax=plt.subplots()
#变量fig表示由生成的一系列绘图构成的整个图形,变量ax表示图形中的绘图
ax.plot(input_values,squares,linewidth=3)#参数linewidth决定了plot()绘制的线条的粗细

#设置图题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

#设置刻度标记的样式
ax.tick_params(axis='both',labelsize=14)#将两条上的刻度字号都设置为14
plt.show()
