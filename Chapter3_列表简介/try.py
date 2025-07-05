#3-1 姓名
names=["han chengzhi","lin shitian","huang xiangdong"]
print(names[0])
print(names[1])
print(names[-1])

#3-2 问候语
print('\n')
print(names[0].title()+" hello,welcome to Python")
print(names[1].title()+" hello,welcome to Python")
print(names[2].title()+" hello,welcome to Python")

#3-3 自己的列表
trafficlist=["bus","car","bicycle","train","plane","subway"]
print("I would like to own a Boying 747 "+trafficlist[4])

#3-4 嘉宾名单
guestlist=["huang xiangdong","han chengzhi","lin shitian","wen nuan"]
print("I want to invite "+guestlist[0].title()+" 、 "+guestlist[1].title()+" and "+guestlist[2].title()+" and "+guestlist[3].title()+" to dinner with me.")

#3-5 修改嘉宾名单
print("Han Chengzhi can't come to dinner.")
guestlist[1]="chen zhi"
print("I want to invite "+guestlist[0].title()+" 、 "+guestlist[1].title()+" and "+guestlist[2].title()+" and "+guestlist[3].title()+" to dinner with me.")

#3-6 添加嘉宾
print("I found a bigger table.")
guestlist.insert(0,"gao xin")
print("I want to invite "+guestlist[0].title()+" 、 "+guestlist[1].title()+" 、 "+guestlist[2].title()+" and "+guestlist[3].title()+" and "+guestlist[4].title()+" to dinner with me.")

guestlist.insert(2,"guo hao")
print("I want to invite "+guestlist[0].title()+" 、 "+guestlist[1].title()+" 、 "+guestlist[2].title()+" and "+guestlist[3].title()+" and "+guestlist[4].title()+" and "+guestlist[5].title()+" to dinner with me.")

guestlist.append("zhao dengqi")
print("I want to invite "+guestlist[0].title()+" 、 "+guestlist[1].title()+" 、 "+guestlist[2].title()+" and "+guestlist[3].title()+" and "+guestlist[4].title()+" and "+guestlist[5].title()+" and "+guestlist[6].title()+" to dinner with me.")

#3-7 缩减名单
print("I can only invite two people to dinner.")
print(guestlist.pop().title()+",I'm sorry I can't invite you to dinner.")
print(guestlist.pop().title()+",I'm sorry I can't invite you to dinner.")
print(guestlist.pop().title()+" I'm sorry I can't invite you to dinner.")
print(guestlist.pop().title()+" I'm sorry I can't invite you to dinner.")
print(guestlist.pop().title()+" I'm sorry I can't invite you to dinner.")

print(guestlist[0]+" I'm still inviting you to dinner.")
print(guestlist[1]+" I'm still inviting you to dinner.")
del guestlist[1]
del guestlist[0]
print(guestlist)

#3-8 放眼世界
places=["beijing","shanghai","guangzhou","hangzhou","shenzhen"]
print("Here is the original list:")
print(places)
print(sorted(places))
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)

#3-9 晚餐嘉宾
print(len(places))

#3-10 尝试使用各个函数
