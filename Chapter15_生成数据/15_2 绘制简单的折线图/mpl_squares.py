import matplotlib.pyplot as plt

squares=[1, 4, 9, 16, 25]
fig,ax=plt.subplots()
"""fig, ax = plt.subplots() 是 Matplotlib 中用于创建图形和子图的代码。  
plt.subplots() 会同时创建一个图形对象 (fig) 和一个或多个子图对象 (ax)。
fig 是图形对象，表示整个绘图区域。
ax 是子图对象，表示图形中的一个绘图区域（轴）。"""
ax.plot(squares)
"""squares 是一个列表，包含要绘制的 y 轴数据 [1, 4, 9, 16, 25]。
ax.plot(squares) 会根据列表中的值绘制一条折线，x 轴的值默认为 [0, 1, 2, 3, 4]（索引值）。
折线图会显示在 ax（子图）中。"""
plt.show()