import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

plt.style.use('seaborn-v0_8')  # 使用seaborn-v0_8样式
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=100)#s=200是点的尺寸

#设置图题并给坐标轴加上标签
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)

#设置刻度标记的样式
ax.tick_params(labelsize=14)
plt.show()