#5-1 条件测试
from traceback import print_tb

car='subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')
print("\nIs car=='audi'? I predict False.")
print(car=='audi')

#5-2 更多的条件测试
print("\n")
print("huangxiangdong"=="hanchengzhi")
print("huangxiangdong"=="HUANGXIANGDONG".lower())
print(2==2,2!=3,2>1,2<3,2>=2,2<=3)
if 21>20 and 21<22:
    print("21>20 and 21<22")
university=['sdu','zju','whu','hust']
print("sdu" in university)
print("nju" not in university)

#5-3 外星人颜色#1
alien_color='green'
if alien_color=='green':
    print("players get 5 points.")

#5-4 外星人颜色#2
alien_color='red'
if alien_color=='green':
    print("players get 5 points.")
else:
    print("players get 10 points.")

#5-5 外星人颜色#3
alien_color='yellow'
if alien_color=='green':
    print("players get 5 points.")
elif alien_color=='red':
    print("players get 10 points.")
else:
    print("players get 15 points.")

#5-6 人生的不同阶段
age=22
if age<2:
    print("baby")
elif age<4:
    print("walk")
elif age<13:
    print("child")
elif age<20:
    print("teenager")
elif age<65:
    print("adult")
else:
    print("old")

#5-7 喜欢的水果
favorite_fruits=['apple','banana','orange','blueberry']
if 'apple' in favorite_fruits:
    print("You really like apple.")
if 'banana' in favorite_fruits:
    print("You really like banana.")
if 'orange' in favorite_fruits:
    print("You really like orange.")
if 'blueberry' in favorite_fruits:
    print("You really like blueberry.")

#5-8 以特殊方式跟管理员打招呼
usernames=['admin','huang','zhang','li','wang']
for username in usernames:
    if username=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+username+", thank you for logging in again.")

#5-9 处理用户为空的情况
if usernames:
    for username in usernames:
        if username=='admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+username+", thank you for logging in again.")
else:
    print("We need to find some users!")

#5-11 检查用户名
current_users=['huang','zhang','li','wang','admin']
new_users=['guo','zhang','li','han','lin']
for new_user in new_users:
    if new_user in current_users:
        print("This username has been used.")
    else:
        print("This username isn't used.")

#5-12 序数
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print(str(number)+"st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    elif number==4:
        print(str(number)+"th")
    elif number==5:
        print(str(number)+"th")
    elif number==6:
        print(str(number)+"th")
    elif number==7:
        print(str(number)+"th")
    elif number==8:
        print(str(number)+"th")
    elif number==9:
        print(str(number)+"th")


