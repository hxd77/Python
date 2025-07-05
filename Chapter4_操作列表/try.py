#4-1 比萨：
pizzas=["pepperoni","mushrooms","extra cheese"]
for pizza in pizzas:
    print("I like "+pizza.title()+" pizza.")
print("I really love pizza!")

#4-2 动物：
animals=["cat","dog","rabbit"]
for animal in animals:
    print("A "+animal.title()+" would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3 数到20：
for value in range(1,21):
    print(value)

#4-4 一百万：
#for value in range(1,1000001):
    #print(value)


#4-5 计算1~1000000的总和
#numbers=[num for num in range(1,1000001)]
#print(sum(numbers))

#4-6 奇数：
#odd_numbers=[num for num in range(1,21,2)]
#print(odd_numbers)

#4-7 3的倍数：
three_numbers=[num for num in range(3,31,3)]
print(three_numbers)

#4-8 立方：
#cubes=[]
#for num in range(11):
    #cube=num**3
    #cubes.append(cube)
    #print(cube)
#print(cubes)

#4-9 立方解析
#cubes=[cube**3 for cube in range(1,11)]
#print(cubes)

#4-10 切片
places=['america','canada','japan','china','korea']
print("The first three items in the list are: ",places[:3])
print("The items from the middle of the list are: ",places[1:4])
print("The items from the last three items in the list are: ",places[2:])

#4-11 你的比萨和我的比萨
friend_pizzas=pizzas[:]
pizzas.append('apple')
friend_pizzas.append('banana')
print("My favorite pizzas are:",pizzas)
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:",friend_pizzas)
for friend_pizza in friend_pizzas:
    print(friend_pizza)

#4-13 自助餐
foods=('beef','chicken','fish','pig','apple')
for food in foods:
    print(food)
foods=('beef','chicken','fish','blueberry','banana')
for food in foods:
    print(food)