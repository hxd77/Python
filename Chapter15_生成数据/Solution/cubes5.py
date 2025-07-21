import matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[1,8,27,64,125]

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=40)

ax.set_title("Cubes",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Value",fontsize=14)

ax.tick_params(labelsize=14)

plt.show()