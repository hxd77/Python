import matplotlib.pyplot as plt

x_values=range(1,5001)
y_values=[x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,s=10)

ax.set_title("Cubes",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Value",fontsize=14)

ax.tick_params(labelsize=14)
plt.show()