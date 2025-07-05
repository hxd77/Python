#7-1 汽车租赁
message='\nWhat kind of car would you like to rent? '
car=input(message)
print('Let me see if I can find you a '+car+'.' )

#7-2 餐馆预定
num=int(input("How many people are in your dinner group? "))
if num>8:
    print("There is not empty table.")
else:
    print("There is empty table.")

#7-3 10的整数倍
number=int(input("Please enter a number: "))
if number%10==0:
    print(str(number)+" is a multiple of 10.")
else:
    print(str(number)+" is not a multiple of 10.")

#7-4 比萨配料
prompt="\nPlease enter the pizza toppings you want to add to your pizza. "
prompt+="\nEnter 'quit' when you are finished. "
while True:
    topping=input(prompt)
    if topping=='quit':
        break
    else:
        print("Adding "+topping+" to your pizza.")

#7-5 电影票
prompt="\nPlease enter your age: "
while True:
    age=int(input(prompt))
    if age<3:
        print("Free")
        break
    elif age<12:
        print("$10")
        break
    else:
        print("$15")
        break

#7-6 三个出口

#7-7 无限循环

#7-8 熟食店
sandwich_orders=['apple_sandwich','banana_sandwich','blueberry_sandwich']
finished_sandwich=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("I made your tuna sandwich")
    finished_sandwich.append(sandwich)
print("Done")
print(finished_sandwich)

#7-9 五香烟熏牛肉（pastrami）卖完了
sandwich_orders=['apple_sandwich','banana_sandwich','blueberry_sandwich','pastrami','pastrami','pastrami']
print("Pastrami is sold out")
while  'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwich=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print("I made your tuna sandwich")
    finished_sandwich.append(sandwich)
print("Done")
print(finished_sandwich)

#7-10 梦想的度假胜地
