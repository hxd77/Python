alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0["points"])
new_points=alien_0['points']
print("You just earned "+str(new_points)+" points.")
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
print("The alien is "+alien_0['color'])
alien_0['color']='yellow'
print("The alien is "+alien_0['color'])

alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

#向右移动外星人
#据外星人当前速度决定其移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: "+str(alien_0['x_position']))

alien_0={'color':'green','points':5}
del alien_0['color']
print(alien_0)

