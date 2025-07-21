import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]#列表推导式

plt.style.use('seaborn-v0_8')  # 使用seaborn-v0_8样式
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)#c代表y值坐标,表示颜色映射,s=200是点的尺寸

#设置图题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

#设置每个坐标轴的取值范围#实际测试加或不加都一样
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')#使用常规刻度标记

#设置刻度标记的样式刻度标记字号为14
ax.tick_params(labelsize=14)
plt.savefig('squares_plot.png',bbox_inches='tight')
#保存图片到当前目录，第二个参数表示裁剪掉绘图多余空白区域
